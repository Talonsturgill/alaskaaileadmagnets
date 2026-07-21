/* cf-spine.js — Case Files deck 001 shared spine painter.
   The count-baseline panorama: all spine art is a pure function of
   globalX = slideIndex*1080 + localX so adjacent slides seam exactly.
   Requires noise.js (AK.*) loaded first. Draw in CSS px (ctx pre-scaled 2x).
   Committed as a run asset; later decks write their own spine or none. */
(function () {
  const W = 1080, H = 1350;
  const BASE_SEED = 20260721;
  const BASELINE_Y = 880;

  function bedY(gx) {
    return 1120 + AK.fbm2(gx * 0.0012, 7.3, 4) * 90;
  }

  const CF = {
    W, H, BASELINE_Y, BASE_SEED,

    // Background water gradient + faint sonar banding below y=830.
    water(cx, opts = {}) {
      const g = cx.createLinearGradient(0, 0, 0, H);
      g.addColorStop(0, opts.top || '#061A1D');
      g.addColorStop(0.6, opts.mid || '#0A272B');
      g.addColorStop(1, opts.bottom || '#103439');
      cx.fillStyle = g;
      cx.fillRect(0, 0, W, H);
      cx.fillStyle = 'rgba(46,110,106,0.03)';
      for (let y = 830; y < H; y += 7) cx.fillRect(0, y, W, 1);
    },

    // Teal mesh-wash radials, seeded per slide for variety, alpha kept low.
    wash(cx, slideIndex, n = 5) {
      const rng = AK.rng(BASE_SEED + slideIndex * 17 + 3);
      for (let i = 0; i < n; i++) {
        const x = rng() * W, y = 200 + rng() * 900, r = 260 + rng() * 380;
        const g = cx.createRadialGradient(x, y, 0, x, y, r);
        const c = i % 2 ? '28,74,78' : '46,110,106';
        g.addColorStop(0, `rgba(${c},0.10)`);
        g.addColorStop(1, `rgba(${c},0)`);
        cx.fillStyle = g;
        cx.beginPath(); cx.arc(x, y, r, 0, Math.PI * 2); cx.fill();
      }
    },

    // The riverbed + baseline rule for this slide. Pure globalX functions.
    spine(cx, slideIndex, opts = {}) {
      const off = slideIndex * W;
      // Riverbed silhouette.
      cx.beginPath();
      cx.moveTo(0, H);
      for (let x = 0; x <= W; x += 6) cx.lineTo(x, bedY(off + x));
      cx.lineTo(W, H);
      cx.closePath();
      cx.fillStyle = opts.bedFill || '#05161A';
      cx.fill();
      // The count baseline, the human count, never moves.
      if (opts.baseline !== false) {
        cx.strokeStyle = opts.baselineColor || 'rgba(159,178,184,0.85)';
        cx.lineWidth = opts.baselineWidth || 2.5;
        cx.beginPath();
        cx.moveTo(0, BASELINE_Y); cx.lineTo(W, BASELINE_Y);
        cx.stroke();
      }
    },

    // Suspended silt, denser near the bed, seeded by globalX bucket so the
    // field continues across the seam.
    silt(cx, slideIndex, count = 240) {
      const off = slideIndex * W;
      const rng = AK.rng(BASE_SEED + 71);
      for (let i = 0; i < count * 8; i++) {
        const gx = rng() * W * 8, y = 180 + rng() * (H - 260);
        if (gx < off || gx >= off + W) continue;
        const x = gx - off;
        const nearBed = Math.max(0, 1 - Math.abs(bedY(gx) - y) / 520);
        if (rng() > 0.35 + nearBed * 0.5) continue;
        const r = 0.6 + rng() * 1.7;
        cx.fillStyle = `rgba(143,184,174,${(0.04 + rng() * 0.09).toFixed(3)})`;
        cx.beginPath(); cx.arc(x, y, r, 0, Math.PI * 2); cx.fill();
      }
    },

    // Hand tally strokes in bundles of five. opts: color, h, weight,
    // fracturedEvery (render every Nth stroke broken), maxOnSlide.
    tally(cx, xStart, y, count, opts = {}) {
      const gap = opts.gap || 9, bundleGap = opts.bundleGap || 14;
      const h = opts.h || 34, w = opts.weight || 2;
      let x = xStart, drawn = 0;
      for (let i = 0; i < count; i++) {
        if (x > (opts.maxX || W + 40)) break;
        const inBundle = i % 5;
        cx.strokeStyle = opts.color || '#FFC72C';
        cx.lineWidth = w;
        cx.lineCap = 'round';
        const frac = opts.fracturedEvery && ((i % opts.fracturedEvery) === opts.fracturedEvery - 1);
        cx.beginPath();
        if (inBundle === 4) {
          cx.moveTo(x - 4 * gap - 4, y + h * 0.15);
          cx.lineTo(x + 4, y + h * 0.85);
        } else if (frac) {
          cx.moveTo(x, y); cx.lineTo(x, y + h * 0.38);
          cx.moveTo(x, y + h * 0.62); cx.lineTo(x, y + h);
        } else {
          cx.moveTo(x, y); cx.lineTo(x, y + h);
        }
        cx.stroke();
        x += (inBundle === 4) ? bundleGap : gap;
        drawn++;
      }
      return drawn;
    },

    // Weir pickets crossing the baseline. xs in CSS px.
    pickets(cx, xFrom, xTo, opts = {}) {
      const spacing = opts.spacing || 46;
      for (let x = xFrom; x <= xTo; x += spacing) {
        const g = cx.createLinearGradient(0, opts.top || 700, 0, opts.bottom || 1180);
        g.addColorStop(0, opts.hi || '#6C818A');
        g.addColorStop(1, opts.lo || '#12262A');
        cx.fillStyle = g;
        cx.fillRect(x, opts.top || 700, opts.w || 10, (opts.bottom || 1180) - (opts.top || 700));
        // waterline glint
        cx.fillStyle = 'rgba(196,212,208,0.25)';
        cx.fillRect(x, BASELINE_Y - 2, opts.w || 10, 3);
      }
    },

    // Phantom-dash rectangle path helper for PROPOSED elements.
    phantomRect(cx, x, y, w, h, color = 'rgba(159,178,184,0.45)') {
      cx.save();
      cx.strokeStyle = color;
      cx.lineWidth = 2;
      cx.setLineDash([4, 8]);
      cx.strokeRect(x, y, w, h);
      cx.restore();
    },

    // Dawn light shafts, alpha kept whisper-low.
    shafts(cx, slideIndex, n = 2) {
      const rng = AK.rng(BASE_SEED + slideIndex * 5 + 29);
      for (let i = 0; i < n; i++) {
        const x0 = 140 + rng() * 800, tilt = 120 + rng() * 160, w0 = 60 + rng() * 90;
        const g = cx.createLinearGradient(x0, 0, x0 + tilt, 1000);
        g.addColorStop(0, 'rgba(196,212,208,0.07)');
        g.addColorStop(1, 'rgba(196,212,208,0)');
        cx.fillStyle = g;
        cx.beginPath();
        cx.moveTo(x0, 0); cx.lineTo(x0 + w0, 0);
        cx.lineTo(x0 + tilt + w0 * 1.6, 1000); cx.lineTo(x0 + tilt, 1000);
        cx.closePath(); cx.fill();
      }
    },

    // A sockeye silhouette, body olive, back brick, drawn at (x,y) length L,
    // swimming right (flip=-1 to swim left).
    sockeye(cx, x, y, L = 120, flip = 1) {
      cx.save();
      cx.translate(x, y); cx.scale(flip, 1);
      cx.fillStyle = '#4A7A54';
      cx.beginPath();
      cx.moveTo(-L * 0.5, 0);
      cx.quadraticCurveTo(-L * 0.15, -L * 0.16, L * 0.28, -L * 0.05);
      cx.quadraticCurveTo(L * 0.42, -L * 0.02, L * 0.5, -L * 0.1);
      cx.lineTo(L * 0.44, 0);
      cx.lineTo(L * 0.5, L * 0.1);
      cx.quadraticCurveTo(L * 0.42, L * 0.02, L * 0.28, L * 0.05);
      cx.quadraticCurveTo(-L * 0.15, L * 0.16, -L * 0.5, 0);
      cx.closePath(); cx.fill();
      cx.fillStyle = 'rgba(122,74,60,0.85)';
      cx.beginPath();
      cx.moveTo(-L * 0.5, 0);
      cx.quadraticCurveTo(-L * 0.15, -L * 0.16, L * 0.28, -L * 0.05);
      cx.quadraticCurveTo(L * 0.1, -L * 0.01, -L * 0.5, 0);
      cx.closePath(); cx.fill();
      cx.restore();
    },

    // Sonar wedge fan (ARIS style) centered cxr,cyr radius R, amber rings,
    // seeded fish blips. Returns blip list.
    sonarWedge(cx, cxr, cyr, R, slideIndex, opts = {}) {
      const a0 = -0.62, a1 = 0.62, rot = opts.rot || -1.5708;
      cx.save();
      cx.translate(cxr, cyr); cx.rotate(rot);
      cx.fillStyle = opts.panel || 'rgba(10,39,43,0.92)';
      cx.beginPath(); cx.moveTo(0, 0); cx.arc(0, 0, R, a0, a1); cx.closePath(); cx.fill();
      for (let k = 1; k <= (opts.rings || 7); k++) {
        cx.beginPath(); cx.arc(0, 0, (R / (opts.rings || 7)) * k, a0, a1);
        cx.strokeStyle = `rgba(233,161,60,${(0.34 - k * 0.033).toFixed(3)})`;
        cx.lineWidth = 1.6; cx.stroke();
      }
      for (const s of [-1, 1]) {
        cx.beginPath(); cx.moveTo(0, 0);
        cx.lineTo(Math.cos(s > 0 ? a1 : a0) * R, Math.sin(s > 0 ? a1 : a0) * R);
        cx.strokeStyle = 'rgba(233,161,60,0.28)'; cx.lineWidth = 1.6; cx.stroke();
      }
      const rng = AK.rng(BASE_SEED + slideIndex * 13 + 7);
      const blips = [];
      for (let i = 0; i < (opts.blips || 12); i++) {
        const a = a0 + 0.08 + rng() * (a1 - a0 - 0.16);
        const r = R * (0.22 + rng() * 0.7);
        const bx = Math.cos(a) * r, by = Math.sin(a) * r;
        cx.beginPath();
        cx.ellipse(bx, by, 9 + rng() * 5, 3.6 + rng() * 1.8, a, 0, Math.PI * 2);
        cx.fillStyle = `rgba(240,180,90,${(0.5 + rng() * 0.35).toFixed(3)})`;
        cx.fill();
        blips.push([bx, by]);
      }
      // scanline texture
      cx.globalAlpha = 0.05;
      for (let y = -R; y < R; y += 5) { cx.fillStyle = '#061A1D'; cx.fillRect(-R, y, R * 2, 1); }
      cx.globalAlpha = 1;
      cx.restore();
      return blips;
    },

    // Fine grain pass, call last on the art canvas.
    grain(cx, amount = 6, seed = 9902) {
      const img = cx.getImageData(0, 0, W * 2, H * 2);
      const d = img.data;
      const rng = AK.rng(seed);
      for (let p = 0; p < d.length; p += 4) {
        const n = (rng() - 0.5) * amount;
        d[p] += n; d[p + 1] += n; d[p + 2] += n;
      }
      cx.putImageData(img, 0, 0);
    }
  };

  window.CF = CF;
})();
