import base64, os
D = os.path.dirname(os.path.abspath(__file__))

def b64(f, mime):
    with open(os.path.join(D, f), 'rb') as fh:
        return f"data:{mime};base64," + base64.b64encode(fh.read()).decode()

main_src    = b64('main_window_scanning.png', 'image/png')
filter_src  = b64('filter_feature.png',       'image/png')
preview_src = b64('preview_dialog.png',        'image/png')
video_src   = b64('deep_scanning.mp4',         'video/mp4')

html = f"""<title>Resurgex — Windows File Recovery</title>

<style>
/* ── Tokens ─────────────────────────────────────────────── */
:root {{
  --bg:       #07090E;
  --surface:  #0D1521;
  --card:     #111E2E;
  --border:   #1A2B3D;
  --text:     #D8E8F5;
  --muted:    #5E7890;
  --accent:   #1A9BEE;
  --aclo:     rgba(26,155,238,.12);
  --green:    #20D47A;
  --orange:   #FF7A45;
  --mono:     'Cascadia Code','Consolas','Courier New',monospace;
  --sans:     'Segoe UI',-apple-system,system-ui,sans-serif;
  --r:        8px;
}}
@media (prefers-color-scheme: light) {{ :root {{
  --bg:       #EDF2F8; --surface:  #FFFFFF; --card:     #FFFFFF;
  --border:   #C5D5E5; --text:     #0A1828; --muted:    #5070A0;
  --accent:   #0B80D0; --aclo:     rgba(11,128,208,.1);
  --green:    #0EA860; --orange:   #D45A20;
}}}}
:root[data-theme="light"] {{
  --bg:#EDF2F8;--surface:#FFFFFF;--card:#FFFFFF;--border:#C5D5E5;
  --text:#0A1828;--muted:#5070A0;--accent:#0B80D0;
  --aclo:rgba(11,128,208,.1);--green:#0EA860;--orange:#D45A20;
}}
:root[data-theme="dark"] {{
  --bg:#07090E;--surface:#0D1521;--card:#111E2E;--border:#1A2B3D;
  --text:#D8E8F5;--muted:#5E7890;--accent:#1A9BEE;
  --aclo:rgba(26,155,238,.12);--green:#20D47A;--orange:#FF7A45;
}}

/* ── Reset ──────────────────────────────────────────────── */
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-behavior:smooth}}
body{{font-family:var(--sans);background:var(--bg);color:var(--text);
  line-height:1.6;font-size:15px;-webkit-font-smoothing:antialiased}}
a{{color:var(--accent);text-decoration:none}}
a:hover{{text-decoration:underline}}

/* ── Buttons ────────────────────────────────────────────── */
.btn{{display:inline-flex;align-items:center;justify-content:center;gap:8px;
  padding:10px 22px;border-radius:var(--r);font-family:var(--sans);
  font-size:14px;font-weight:600;cursor:pointer;border:1.5px solid transparent;
  transition:opacity .15s,border-color .15s,color .15s;
  white-space:nowrap;text-decoration:none!important}}
.btn-accent{{background:var(--accent);color:#fff;border-color:var(--accent)}}
.btn-accent:hover{{opacity:.85}}
.btn-ghost{{background:transparent;color:var(--text);border-color:var(--border)}}
.btn-ghost:hover{{border-color:var(--accent);color:var(--accent)}}
.btn-lg{{padding:14px 30px;font-size:15px}}
.btn-full{{width:100%}}

/* ── Nav ────────────────────────────────────────────────── */
.nav{{position:sticky;top:0;z-index:100;background:var(--bg);border-bottom:1px solid var(--border)}}
.nav-in{{max-width:1120px;margin:0 auto;padding:0 24px;height:60px;
  display:flex;align-items:center;justify-content:space-between}}
.logo{{display:flex;align-items:center;gap:10px;font-weight:700;font-size:17px;
  color:var(--text);text-decoration:none!important}}
.logo-mark{{width:30px;height:30px;background:var(--accent);border-radius:7px;
  display:flex;align-items:center;justify-content:center;
  font-family:var(--mono);font-size:11px;font-weight:700;color:#fff}}
.nav-btns{{display:flex;gap:10px}}

/* ── Layout ─────────────────────────────────────────────── */
.wrap{{max-width:1120px;margin:0 auto;padding:0 24px}}

/* ── Hero ───────────────────────────────────────────────── */
.hero{{padding:88px 0 96px}}
.hero-in{{max-width:1120px;margin:0 auto;padding:0 24px;
  display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:center}}
.eyebrow{{font-family:var(--mono);font-size:11px;text-transform:uppercase;
  letter-spacing:.14em;color:var(--accent);margin-bottom:22px}}
.hero h1{{font-size:clamp(34px,5vw,52px);font-weight:700;line-height:1.08;
  letter-spacing:-.025em;text-wrap:balance;margin-bottom:22px}}
.hero-sub{{font-size:16px;color:var(--muted);line-height:1.75;
  max-width:460px;margin-bottom:36px}}
.hero-btns{{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:22px}}
.hero-meta{{font-family:var(--mono);font-size:11px;color:var(--muted);letter-spacing:.04em}}

/* ── Demo video ─────────────────────────────────────────── */
.demo-video{{
  width:100%;display:block;border-radius:11px;
  border:1px solid var(--border);
  box-shadow:0 32px 80px rgba(0,0,0,.5),0 0 0 1px var(--border);
}}

/* ── Section chrome ─────────────────────────────────────── */
.section{{padding:80px 0;border-top:1px solid var(--border)}}
.sec-label{{font-family:var(--mono);font-size:11px;text-transform:uppercase;
  letter-spacing:.14em;color:var(--accent);margin-bottom:12px}}
.sec-title{{font-size:clamp(26px,3vw,36px);font-weight:700;
  letter-spacing:-.02em;text-wrap:balance;margin-bottom:48px}}

/* ── Features ───────────────────────────────────────────── */
.feat-grid{{display:grid;grid-template-columns:repeat(3,1fr);
  gap:1px;background:var(--border);
  border:1px solid var(--border);border-radius:10px;overflow:hidden}}
.feat-card{{background:var(--card);padding:28px 24px}}
.feat-icon{{width:38px;height:38px;background:var(--aclo);border-radius:var(--r);
  display:flex;align-items:center;justify-content:center;font-size:17px;margin-bottom:16px}}
.feat-name{{font-weight:700;font-size:14px;margin-bottom:8px}}
.feat-desc{{font-size:13px;color:var(--muted);line-height:1.65}}

/* ── Screenshots ────────────────────────────────────────── */
.shots{{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}}
.shot img{{
  width:100%;display:block;border-radius:8px;
  border:1px solid var(--border);
  box-shadow:0 8px 32px rgba(0,0,0,.35);
  transition:transform .2s,box-shadow .2s;
}}
.shot img:hover{{transform:translateY(-3px);box-shadow:0 16px 48px rgba(0,0,0,.45)}}
.shot-cap{{font-size:12px;color:var(--muted);text-align:center;margin-top:10px;
  font-family:var(--mono)}}

/* ── How ────────────────────────────────────────────────── */
.steps{{display:grid;grid-template-columns:repeat(3,1fr);gap:48px}}
.step-n{{font-family:var(--mono);font-size:38px;font-weight:700;
  color:var(--border);line-height:1;margin-bottom:18px}}
.step-t{{font-size:16px;font-weight:700;margin-bottom:10px}}
.step-d{{font-size:13px;color:var(--muted);line-height:1.65}}

/* ── Pricing ────────────────────────────────────────────── */
.price-wrap{{max-width:460px;margin:0 auto}}
.price-card{{background:var(--card);border:1px solid var(--border);border-radius:12px;overflow:hidden}}
.price-head{{padding:36px 36px 28px;border-bottom:1px solid var(--border);text-align:center}}
.price-tier{{font-family:var(--mono);font-size:11px;text-transform:uppercase;
  letter-spacing:.12em;color:var(--muted);margin-bottom:20px}}
.price-num{{font-size:56px;font-weight:800;letter-spacing:-.035em;line-height:1;margin-bottom:10px}}
.price-num sup{{font-size:24px;font-weight:700;vertical-align:top;margin-top:10px;display:inline-block}}
.price-once{{font-size:14px;color:var(--green);font-weight:600}}
.price-list{{list-style:none;padding:28px 36px;display:flex;flex-direction:column;gap:13px}}
.price-list li{{display:flex;align-items:flex-start;gap:12px;font-size:14px}}
.price-list li::before{{content:'✓';color:var(--green);font-weight:700;flex-shrink:0;margin-top:1px}}
.price-btns{{padding:0 36px 36px;display:flex;flex-direction:column;gap:10px}}

/* ── Requirements ───────────────────────────────────────── */
.reqs{{display:grid;grid-template-columns:repeat(4,1fr);gap:24px}}
.req-l{{font-family:var(--mono);font-size:11px;text-transform:uppercase;
  letter-spacing:.1em;color:var(--muted);margin-bottom:7px}}
.req-v{{font-size:14px;font-weight:600}}

/* ── Footer ─────────────────────────────────────────────── */
.footer{{border-top:1px solid var(--border);padding:32px 0}}
.footer-in{{max-width:1120px;margin:0 auto;padding:0 24px;
  display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap}}
.footer-copy{{font-size:13px;color:var(--muted)}}
.footer-qt{{font-size:12px;color:var(--muted)}}

/* ── Responsive ─────────────────────────────────────────── */
@media(max-width:880px){{
  .hero-in{{grid-template-columns:1fr;gap:44px}}
  .feat-grid{{grid-template-columns:1fr 1fr}}
  .steps{{grid-template-columns:1fr;gap:36px}}
  .reqs{{grid-template-columns:1fr 1fr}}
  .shots{{grid-template-columns:1fr}}
}}
@media(max-width:560px){{
  .feat-grid{{grid-template-columns:1fr}}
  .nav-btns .btn-ghost{{display:none}}
  .hero-btns{{flex-direction:column}}
  .hero-btns .btn{{width:100%}}
  .shots{{grid-template-columns:1fr}}
}}
</style>

<nav class="nav">
  <div class="nav-in">
    <a class="logo" href="#">
      <div class="logo-mark">Rx</div>Resurgex
    </a>
    <div class="nav-btns">
      <a href="#download" class="btn btn-ghost">Download Trial</a>
      <a href="#buy" class="btn btn-accent">Buy — $24.95</a>
    </div>
  </div>
</nav>

<section class="hero">
  <div class="hero-in">
    <div>
      <div class="eyebrow">Windows File Recovery</div>
      <h1>Your deleted files aren't gone yet.</h1>
      <p class="hero-sub">Resurgex scans past the filesystem into raw sectors — recovering photos, documents, and archives that other tools miss. Pay once, own it forever.</p>
      <div class="hero-btns">
        <a href="#download" class="btn btn-accent btn-lg">Download Free Trial</a>
        <a href="#buy" class="btn btn-ghost btn-lg">Buy Now — $24.95</a>
      </div>
      <div class="hero-meta">Windows 10 / 11 &nbsp;·&nbsp; 64-bit &nbsp;·&nbsp; No internet required</div>
    </div>
    <div>
      <video class="demo-video" autoplay muted loop playsinline>
        <source src="{video_src}" type="video/mp4">
      </video>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-label">Capabilities</div>
    <h2 class="sec-title">Everything you need to get files back.</h2>
    <div class="feat-grid">
      <div class="feat-card">
        <div class="feat-icon">🔍</div>
        <div class="feat-name">Deep Sector Scan</div>
        <div class="feat-desc">Signature carving reads raw sectors to find files by their magic bytes — even when the filesystem is completely wiped or corrupt.</div>
      </div>
      <div class="feat-card">
        <div class="feat-icon">🗂️</div>
        <div class="feat-name">NTFS · FAT32 · exFAT</div>
        <div class="feat-desc">Full directory scan for all three major Windows filesystems. Reads original filenames, paths, and sizes where the metadata is intact.</div>
      </div>
      <div class="feat-card">
        <div class="feat-icon">💾</div>
        <div class="feat-name">Physical Drive Support</div>
        <div class="feat-desc">Access deleted or unmounted partitions directly through the raw disk — no drive letter or mounted volume required.</div>
      </div>
      <div class="feat-card">
        <div class="feat-icon">👁️</div>
        <div class="feat-name">File Preview</div>
        <div class="feat-desc">Preview images, documents, and PDFs inside the app before recovery. Confirm the file is intact before writing it anywhere.</div>
      </div>
      <div class="feat-card">
        <div class="feat-icon">🖼️</div>
        <div class="feat-name">Disk Imaging</div>
        <div class="feat-desc">Clone a failing drive sector-by-sector to a safe image file. Stop the clock on a dying disk and recover from the image at your own pace.</div>
      </div>
      <div class="feat-card">
        <div class="feat-icon">⚡</div>
        <div class="feat-name">Modern Interface</div>
        <div class="feat-desc">Live sector map, real-time progress, file filtering by type and size, and pause/resume. Designed for how data recovery actually works.</div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-label">Screenshots</div>
    <h2 class="sec-title">See it in action.</h2>
    <div class="shots">
      <div class="shot">
        <img src="{main_src}" alt="Resurgex scanning a drive with live sector map">
        <div class="shot-cap">Deep scan with live sector map</div>
      </div>
      <div class="shot">
        <img src="{preview_src}" alt="File preview dialog">
        <div class="shot-cap">Preview files before recovery</div>
      </div>
      <div class="shot">
        <img src="{filter_src}" alt="Filter and search results">
        <div class="shot-cap">Filter by type, size, and recovery chance</div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-label">Process</div>
    <h2 class="sec-title">Three steps to recover your files.</h2>
    <div class="steps">
      <div>
        <div class="step-n">01</div>
        <div class="step-t">Select your drive</div>
        <div class="step-d">Choose any connected drive or disk image file. Resurgex detects FAT32, exFAT, and NTFS volumes automatically — including raw physical drives with deleted partitions.</div>
      </div>
      <div>
        <div class="step-n">02</div>
        <div class="step-t">Scan for deleted files</div>
        <div class="step-d">A quick directory scan runs first. If nothing is found, Resurgex offers a deep scan — reading every sector for file signatures across 15+ formats including JPG, PNG, PDF, DOCX, MP4, and more.</div>
      </div>
      <div>
        <div class="step-n">03</div>
        <div class="step-t">Preview and recover</div>
        <div class="step-d">Filter results by name, type, size, or recovery chance. Preview files in-app to confirm they're intact, then recover to any folder on a different drive.</div>
      </div>
    </div>
  </div>
</section>

<section class="section" id="buy">
  <div class="wrap">
    <div class="sec-label">Pricing</div>
    <h2 class="sec-title">One price. No tricks.</h2>
    <div class="price-wrap">
      <div class="price-card">
        <div class="price-head">
          <div class="price-tier">Resurgex</div>
          <div class="price-num"><sup>$</sup>24.95</div>
          <div class="price-once">One-time purchase — own it forever</div>
        </div>
        <ul class="price-list">
          <li>Unlimited file recovery — all sizes, all types</li>
          <li>NTFS, FAT32, and exFAT filesystem support</li>
          <li>Deep sector scan across 15+ file signatures</li>
          <li>Physical drive and deleted partition access</li>
          <li>File preview before recovery</li>
          <li>Sector-by-sector disk imaging</li>
          <li>Free future updates</li>
        </ul>
        <div class="price-btns">
          <a href="#" class="btn btn-accent btn-lg btn-full">Buy Now — $24.95</a>
          <a href="#download" class="btn btn-ghost btn-full">Download Free Trial first</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section" id="download">
  <div class="wrap">
    <div class="sec-label">System Requirements</div>
    <div style="margin-bottom:40px"></div>
    <div class="reqs">
      <div><div class="req-l">OS</div><div class="req-v">Windows 10 / 11</div></div>
      <div><div class="req-l">Architecture</div><div class="req-v">64-bit only</div></div>
      <div><div class="req-l">Permissions</div><div class="req-v">Administrator</div></div>
      <div><div class="req-l">Internet</div><div class="req-v">Not required</div></div>
    </div>
  </div>
</section>

<footer class="footer">
  <div class="footer-in">
    <div class="footer-copy">© 2025 Calin Serban · Resurgex</div>
    <div class="footer-qt">Built with <a href="https://qt.io" target="_blank" rel="noopener">Qt 6</a> · Licensed under LGPL v3</div>
  </div>
</footer>
"""

out = os.path.join(D, 'landing.html')
with open(out, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Done — {os.path.getsize(out):,} bytes")
