/* ah-desk.js — the AFTER HOURS DESK chassis for Case File No. 002.
 *
 * One lamplit chart-paper plane on a cabinet-extruded desk. Every slide in the
 * deck paints this first, then draws its own ink ON the paper in graphite.
 *
 * Design law this file enforces:
 *  - All QUANTITIES live as flat ink on the unforeshortened paper, so the deck
 *    keeps parallel projection for every number while still being a lit scene.
 *  - Display type is zoned into the dark ROOM BAND above the paper (y < 356),
 *    which solves headline contrast permanently without scrims.
 *  - ONE key light (the lamp, upper-left, off-canvas) casts every shadow,
 *    always down-and-right. The monitor is a practical: rim + cool fill only,
 *    never a shadow caster.
 *  - AH.S publishes every scale constant so DOM labels can be positioned from
 *    the SAME numbers the canvas drew from (instinct i-006).
 *
 * Requires: noise.js (AK.*), akcolor.js (AKC.*), akpost.js (AKPOST.*).
 * Offline, deterministic, seeded from the run date.
 */
(function (root) {
  'use strict';

  var W = 1080, H = 1350;

  // ---- palette -----------------------------------------------------------
  var P = {
    roomDeep:    '#050B14',
    roomBase:    '#0A1626',
    deskTop:     '#14243A',
    deskWall:    '#0B1728',
    paperLit:    '#F0E9DA',
    paperMid:    '#CFC5B0',
    paperFar:    '#8E8779',
    ink:         '#26313F',
    inkSoft:     '#4A5464',
    inkFaint:    '#8E8779',
    lamp:        '#F5B451',
    lampHalo:    '#FFD79A',
    monitor:     '#4FA8D8',
    monitorRim:  '#7CC4E8',
    redStroke:   '#B4453A',
    redText:     '#9E3A30',
    gold:        '#FFC72C',
    shadowTight: '#030710',
    shadowWide:  '#061020'
  };

  // ---- geometry + scale constants (published for the DOM) ----------------
  // The paper is rotated -1.4deg about its centre. Its FILL, EDGES, CURL and
  // SHADOW rotate. Nothing else does: every chart and every text block stays
  // axis-aligned, so no quantity is ever drawn on a slant.
  var S = {
    W: W, H: H,
    ROOM_BOTTOM: 356,          // display type lives above this
    PAPER_X0: 72, PAPER_X1: 1008,
    PAPER_Y0: 356, PAPER_Y1: 1176,
    PAPER_ROT: -1.4 * Math.PI / 180,
    DESK_EDGE_Y: 1176,
    MARGIN: 76,                // optical-left for display type and rules
    RULE_X0: 76, RULE_W: 840,  // the Week Rule's canonical span

    PX_PER_MIN_WEEK:  840 / 2400,   // 0.35 px/min -> an 840px rule is a 40h week
    PX_PER_MIN_VISIT: 704 / 16,     // 44 px/min, slide 03 only
    PX_PER_MIN_ZOOM:  630 / 60,     // 10.5 px/min inside the slide 07 callout

    // line weight tokens, assigned by MEANING (never off-token)
    W_HAIR: 0.75, W_FINE: 1.25, W_STD: 2, W_BOLD: 3.5, W_HERO: 5.5
  };
  S.MAG = S.PX_PER_MIN_ZOOM / S.PX_PER_MIN_WEEK;   // 30, printed on slide 07

  // ---- helpers -----------------------------------------------------------
  function lerp(a, b, t) { return a + (b - a) * t; }

  function hex2rgb(h) {
    return [parseInt(h.slice(1, 3), 16), parseInt(h.slice(3, 5), 16), parseInt(h.slice(5, 7), 16)];
  }
  function rgba(h, a) {
    var c = hex2rgb(h);
    return 'rgba(' + c[0] + ',' + c[1] + ',' + c[2] + ',' + a + ')';
  }

  /* Distance-from-lamp falloff in [0,1]. 1 = full in the pool. The lamp is an
   * off-canvas warm source; this is what makes the paper darken toward its far
   * corner and is the reason body text is confined to the pool box. */
  function lampFall(x, y) {
    var lx = 250, ly = 210, r = 900;
    var d = Math.hypot(x - lx, y - ly) / r;
    return Math.max(0, Math.min(1, 1 - d * d * 0.92));
  }
  S.lampFall = lampFall;

  // ---- the chassis painter ----------------------------------------------

  function room(cx) {
    var g = cx.createLinearGradient(0, 0, 0, S.ROOM_BOTTOM + 120);
    g.addColorStop(0, P.roomDeep);
    g.addColorStop(1, P.roomBase);
    cx.fillStyle = g;
    cx.fillRect(0, 0, W, H);
  }

  /* #3 Mesh Wash. Three radial stops: lamp halo, monitor falloff entering from
   * off-canvas right, and a floor bounce. `mood` lets a slide shift which
   * light dominates (the deck's palette arc: vendor slides warm, independent
   * slides cool, close slide dim). */
  function wash(cx, mood) {
    mood = mood || {};
    var lampA    = mood.lamp    == null ? 0.10 : mood.lamp;
    var monitorA = mood.monitor == null ? 0.07 : mood.monitor;

    var g1 = cx.createRadialGradient(250, 210, 0, 250, 210, 520);
    g1.addColorStop(0, rgba(P.lamp, lampA));
    g1.addColorStop(1, rgba(P.lamp, 0));
    cx.fillStyle = g1; cx.fillRect(0, 0, W, H);

    var g2 = cx.createRadialGradient(1180, 620, 0, 1180, 620, 640);
    g2.addColorStop(0, rgba(P.monitor, monitorA));
    g2.addColorStop(1, rgba(P.monitor, 0));
    cx.fillStyle = g2; cx.fillRect(0, 0, W, H);

    var g3 = cx.createRadialGradient(540, 1420, 0, 540, 1420, 700);
    g3.addColorStop(0, rgba(P.deskTop, 0.5));
    g3.addColorStop(1, rgba(P.deskTop, 0));
    cx.fillStyle = g3; cx.fillRect(0, 0, W, H);
  }

  /* #39 Cabinet Extrusion. Desk front edge at y=1176, depth 90 offset down-right
   * at 45deg. The top face picks up the lamp falloff; the front wall is two ramp
   * steps darker. */
  function desk(cx) {
    var y = S.DESK_EDGE_Y, d = 90, o = d * 0.7071;

    // top face, lamp-graded left to right
    var g = cx.createLinearGradient(0, y - 40, W, y + 40);
    g.addColorStop(0, P.deskTop);
    g.addColorStop(1, P.roomBase);
    cx.fillStyle = g;
    cx.fillRect(0, y, W, H - y);

    // front wall (the extrusion), darker
    cx.fillStyle = P.deskWall;
    cx.beginPath();
    cx.moveTo(0, y + o); cx.lineTo(W, y + o); cx.lineTo(W, H); cx.lineTo(0, H);
    cx.closePath(); cx.fill();

    // the cut edge itself, a hairline catching the lamp
    cx.strokeStyle = rgba(P.lampHalo, 0.22);
    cx.lineWidth = S.W_HAIR * 2;
    cx.beginPath(); cx.moveTo(0, y); cx.lineTo(W, y); cx.stroke();
  }

  function paperPath(cx) {
    var cxm = (S.PAPER_X0 + S.PAPER_X1) / 2, cym = (S.PAPER_Y0 + S.PAPER_Y1) / 2;
    cx.translate(cxm, cym);
    cx.rotate(S.PAPER_ROT);
    cx.translate(-cxm, -cym);
    cx.beginPath();
    cx.rect(S.PAPER_X0, S.PAPER_Y0, S.PAPER_X1 - S.PAPER_X0, S.PAPER_Y1 - S.PAPER_Y0);
  }

  /* #45 Layered Shadow Elevation, two-part: a tight contact core plus a wide
   * ambient. Shadow colour is a darkened background hue, never black. */
  function paperShadow(cx) {
    cx.save();
    cx.shadowColor = rgba(P.shadowWide, 0.30);
    cx.shadowBlur = 40; cx.shadowOffsetX = 14; cx.shadowOffsetY = 20;
    cx.fillStyle = 'rgba(0,0,0,0.9)';
    paperPath(cx); cx.fill();
    cx.restore();

    cx.save();
    cx.shadowColor = rgba(P.shadowTight, 0.55);
    cx.shadowBlur = 6; cx.shadowOffsetX = 3; cx.shadowOffsetY = 4;
    cx.fillStyle = 'rgba(0,0,0,0.9)';
    paperPath(cx); cx.fill();
    cx.restore();
  }

  /* The chart paper: a radial warm ramp centred in the lamp pool, plus paper
   * tooth drawn as seeded fine noise (a tile, never a full-frame feTurbulence,
   * which would balloon the PDF). */
  function paper(cx, seed) {
    cx.save();
    paperPath(cx);
    cx.clip();

    var g = cx.createRadialGradient(300, 430, 30, 300, 430, 980);
    g.addColorStop(0.00, '#FBF5E6');
    g.addColorStop(0.28, P.paperLit);
    g.addColorStop(0.62, P.paperMid);
    g.addColorStop(1.00, P.paperFar);
    cx.fillStyle = g;
    cx.fillRect(S.PAPER_X0 - 60, S.PAPER_Y0 - 60,
                S.PAPER_X1 - S.PAPER_X0 + 120, S.PAPER_Y1 - S.PAPER_Y0 + 120);

    // paper tooth: fine seeded speckle, kept under the texture budget
    AK.reseed(seed);
    var rnd = AK.rng(seed);
    cx.globalAlpha = 0.055;
    for (var i = 0; i < 5200; i++) {
      var x = S.PAPER_X0 + rnd() * (S.PAPER_X1 - S.PAPER_X0);
      var y = S.PAPER_Y0 + rnd() * (S.PAPER_Y1 - S.PAPER_Y0);
      var v = rnd();
      cx.fillStyle = v > 0.5 ? '#FFFFFF' : '#6B6252';
      cx.fillRect(x, y, 1.4, 1.4);
    }
    cx.globalAlpha = 1;

    // the lamp pool itself, an elliptical warm wash with a soft edge. This is
    // what makes the light read as a LAMP rather than as a flat tint.
    cx.save();
    cx.globalCompositeOperation = 'lighter';
    var lp = cx.createRadialGradient(330, 470, 20, 330, 470, 620);
    lp.addColorStop(0, rgba(P.lampHalo, 0.20));
    lp.addColorStop(0.5, rgba(P.lamp, 0.07));
    lp.addColorStop(1, rgba(P.lamp, 0));
    cx.fillStyle = lp;
    cx.fillRect(S.PAPER_X0 - 60, S.PAPER_Y0 - 60,
                S.PAPER_X1 - S.PAPER_X0 + 120, S.PAPER_Y1 - S.PAPER_Y0 + 120);
    cx.restore();
    cx.restore();
  }

  /* The lifted bottom-left corner. This is the deck's ONE genuinely raised
   * object and it exists to answer the logged lesson that schematic art reads
   * flat unless something is really raised. */
  function curl(cx) {
    cx.save();
    var cxm = (S.PAPER_X0 + S.PAPER_X1) / 2, cym = (S.PAPER_Y0 + S.PAPER_Y1) / 2;
    cx.translate(cxm, cym); cx.rotate(S.PAPER_ROT); cx.translate(-cxm, -cym);

    var x0 = S.PAPER_X0, y1 = S.PAPER_Y1, s = 132, lift = 18;

    // contact shadow under the lifted flap
    cx.save();
    cx.shadowColor = rgba(P.shadowTight, 0.6);
    cx.shadowBlur = 14; cx.shadowOffsetX = 6; cx.shadowOffsetY = 8;
    cx.fillStyle = 'rgba(0,0,0,0.85)';
    cx.beginPath();
    cx.moveTo(x0, y1); cx.lineTo(x0 + s, y1); cx.lineTo(x0, y1 - s);
    cx.closePath(); cx.fill();
    cx.restore();

    // the flap's underside, a darker warm ramp
    var g = cx.createLinearGradient(x0, y1, x0 + s * 0.8, y1 - s * 0.8);
    g.addColorStop(0, '#6E6455');
    g.addColorStop(1, '#B3A992');
    cx.fillStyle = g;
    cx.beginPath();
    cx.moveTo(x0, y1 - lift); cx.lineTo(x0 + s, y1 - lift * 0.2); cx.lineTo(x0, y1 - s);
    cx.closePath(); cx.fill();

    // the fold crease catching the lamp
    cx.strokeStyle = rgba(P.lampHalo, 0.5);
    cx.lineWidth = S.W_FINE;
    cx.beginPath(); cx.moveTo(x0 + s, y1 - lift * 0.2); cx.lineTo(x0, y1 - s); cx.stroke();
    cx.restore();
  }

  /* Blurred keyboard repoussoir, bottom-right, bleeding off two frame edges.
   * Never touches text. This is the "instant expensive lens" foreground. */
  function repoussoir(cx) {
    cx.save();
    cx.filter = 'blur(14px)';
    cx.globalAlpha = 0.85;
    cx.fillStyle = '#0B1524';
    for (var r = 0; r < 3; r++) {
      var y = 1210 + r * 46;
      cx.fillRect(820 + r * 10, y, 300, 34);
    }
    cx.restore();
    cx.filter = 'none';
  }

  /* Cool rim entering from the off-canvas monitor. Practical only, no shadows. */
  function monitorRim(cx, strength) {
    strength = strength == null ? 1 : strength;
    cx.save();
    cx.filter = 'blur(70px)';
    cx.fillStyle = rgba(P.monitor, 0.5 * strength);
    cx.fillRect(1074, 300, 6, 600);
    cx.restore();
    cx.filter = 'none';

    // hard rim on the paper's right / top-right edges only
    cx.save();
    var cxm = (S.PAPER_X0 + S.PAPER_X1) / 2, cym = (S.PAPER_Y0 + S.PAPER_Y1) / 2;
    cx.translate(cxm, cym); cx.rotate(S.PAPER_ROT); cx.translate(-cxm, -cym);
    cx.strokeStyle = rgba(P.monitorRim, 0.45 * strength);
    cx.lineWidth = 2;
    cx.beginPath();
    cx.moveTo(S.PAPER_X1, S.PAPER_Y0);
    cx.lineTo(S.PAPER_X1, S.PAPER_Y1);
    cx.stroke();
    cx.restore();
  }

  /* Paint the whole chassis. Call this FIRST in every slide's renderReady,
   * then draw the slide's own ink, then call AH.finish(cx). */
  function stage(cx, opts) {
    opts = opts || {};
    var seed = opts.seed || 20260725;
    room(cx);
    wash(cx, opts.mood);
    desk(cx);
    paperShadow(cx);
    paper(cx, seed);
    curl(cx);
    monitorRim(cx, opts.monitorRim == null ? 1 : opts.monitorRim);
    if (opts.repoussoir !== false) repoussoir(cx);
  }

  /* The finishing move. Film grade once on the art canvas, after all drawing.
   * IGN dither is ALWAYS on: this deck is nothing but large soft gradients and
   * banding is its top texture risk. */
  function finish(cx, opts) {
    opts = opts || {};
    if (typeof AKPOST !== 'undefined' && AKPOST.grade) {
      AKPOST.grade(cx, {
        w: W, h: H,
        exposure: 0.02,
        saturation: 0.94,
        contrast: 1.08,
        filmic: true,
        lift: [0.008, 0.012, 0.022],       // cool shadow tint, the room
        gain: [1.018, 1.002, 0.972],       // warm highlight tint, the lamp
        vignette: 0.18,
        bloom: { threshold: 0.74, strength: 0.26, radius: 8 },
        grain: { amount: opts.grain == null ? 0.045 : opts.grain, size: 2, seed: 20260725 },
        dither: true,                      // ALWAYS: this deck is all soft gradients
        sharpen: 0.30
      });
    }
  }

  // ---- drafting furniture used across slides -----------------------------

  /* #73 Dimension Call. Extension lines with a 4px object gap and 6px
   * overshoot, dimension line with 3:1 arrowheads. `openRight` draws the right
   * cap as an open phantom dash, which is how a bar encodes "under". */
  function dimension(cx, x0, x1, y, opt) {
    opt = opt || {};
    var col = opt.color || P.ink;
    cx.save();
    cx.strokeStyle = col;
    cx.lineCap = 'butt'; cx.lineJoin = 'miter';

    // extension lines
    cx.lineWidth = S.W_HAIR;
    [x0, x1].forEach(function (x, i) {
      if (i === 1 && opt.openRight) return;
      cx.beginPath();
      cx.moveTo(x, y - (opt.ext || 26));
      cx.lineTo(x, y + 6);
      cx.stroke();
    });

    // dimension line
    cx.lineWidth = opt.weight || S.W_FINE;
    if (opt.dash) { cx.setLineDash(opt.dash); }
    cx.beginPath(); cx.moveTo(x0, y); cx.lineTo(x1, y); cx.stroke();
    cx.setLineDash([]);

    // arrowheads, 3:1 (10 x 3.3)
    function head(x, dir) {
      cx.fillStyle = col;
      cx.beginPath();
      cx.moveTo(x, y);
      cx.lineTo(x - dir * 10, y - 3.3);
      cx.lineTo(x - dir * 10, y + 3.3);
      cx.closePath(); cx.fill();
    }
    if (!opt.noHeadLeft) head(x0, -1);
    if (opt.openRight) {
      // open, phantom cap: the inequality drawn
      cx.strokeStyle = col; cx.lineWidth = S.W_FINE;
      cx.setLineDash([6, 5]);
      cx.beginPath(); cx.moveTo(x1 - 18, y); cx.lineTo(x1 + 14, y); cx.stroke();
      cx.setLineDash([]);
    } else if (!opt.noHeadRight) {
      head(x1, 1);
    }
    cx.restore();
  }

  /* #71 Rule Terminals. ONE flourish deck-wide: a 6px perpendicular tick. */
  function terminal(cx, x, y, color) {
    cx.save();
    cx.strokeStyle = color || P.gold;
    cx.lineWidth = S.W_STD;
    cx.beginPath(); cx.moveTo(x, y - 7); cx.lineTo(x, y + 7); cx.stroke();
    cx.restore();
  }

  /* #75 Hatch Knockout Window. Punch an opaque paper-coloured plate so a
   * numeral never sits on texture and its contrast depends on (text, plate). */
  function knockout(cx, x, y, w, h, color) {
    cx.save();
    cx.fillStyle = color || rgba(P.paperLit, 0.92);
    cx.fillRect(x, y, w, h);
    cx.restore();
  }

  /* #83 Drafting Furniture. The SPEC PLATE: four label-over-value rows naming
   * who measured, with what, on whom, in what unit. No colons anywhere. */
  function specPlate(cx, x, y, rows, opt) {
    opt = opt || {};
    var w = opt.width || 440, rowH = opt.rowH || 40, h = rows.length * rowH + 12;
    cx.save();
    cx.strokeStyle = opt.strong ? P.ink : P.inkFaint;
    cx.lineWidth = opt.strong ? S.W_FINE : S.W_HAIR;
    cx.strokeRect(x, y, w, h);
    cx.beginPath();
    for (var i = 1; i < rows.length; i++) {
      cx.moveTo(x, y + 6 + i * rowH); cx.lineTo(x + w, y + 6 + i * rowH);
    }
    cx.strokeStyle = P.inkFaint; cx.lineWidth = S.W_HAIR; cx.stroke();
    cx.restore();
    return { x: x, y: y, w: w, h: h, rowH: rowH };
  }

  /* #67 phantom dash kit, the deck's two legal dash roles only. */
  var DASH = { phantom: [30, 5, 6, 5, 6, 5], hidden: [7, 4] };

  /* Device B, THE UNIT CHIPS. State is carried by SHAPE, never by brightness:
   * the active unit is a SOLID stroked chip on a plate, the inactive one is a
   * phantom dashed outline with no fill. `active` is 'visit', 'week', 'both'
   * or 'none'. Returns the two label rects so DOM text lands inside them. */
  function unitChips(cx, x, y, active) {
    var CH = 44, PAD = 14, GAP = 24;
    var boxes = [];
    [['PER VISIT', 'visit'], ['PER WEEK', 'week']].forEach(function (c, i) {
      var w = c[0].length * 15.0 + PAD * 2;
      var bx = x + (i ? boxes[0].w + GAP : 0);
      var on = (active === 'both') || (active === c[1]);
      cx.save();
      if (on) {
        cx.fillStyle = rgba(P.paperLit, 0.9);
        cx.fillRect(bx, y, w, CH);
        cx.strokeStyle = P.ink; cx.lineWidth = S.W_FINE;
        cx.setLineDash([]);
      } else {
        cx.strokeStyle = rgba(P.ink, 0.55); cx.lineWidth = S.W_FINE;
        cx.setLineDash([6, 4]);
      }
      cx.strokeRect(bx, y, w, CH);
      cx.setLineDash([]);
      cx.restore();
      boxes.push({ x: bx, y: y, w: w, h: CH, on: on, text: c[0] });
    });
    return boxes;
  }

  root.AH = {
    P: P, S: S, DASH: DASH,
    stage: stage, finish: finish,
    room: room, wash: wash, desk: desk, paper: paper, curl: curl,
    repoussoir: repoussoir, monitorRim: monitorRim,
    dimension: dimension, terminal: terminal, knockout: knockout,
    specPlate: specPlate, unitChips: unitChips,
    rgba: rgba, lerp: lerp, lampFall: lampFall
  };
})(window);
