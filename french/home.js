(() => {
  const comics = (window.NANO_FRENCH_COMICS || [])
    .filter((comic) => !comic.status)
    .sort((a, b) => b.published.localeCompare(a.published));

  const grid = document.getElementById("comic-grid");
  const count = document.getElementById("comic-count");

  count.textContent = String(comics.length);

  grid.innerHTML = comics.map((comic) => {
    const lessonList = comic.lessons.join(" · ");
    return `
      <article class="comic-card">
        <a class="cover-link" href="${escapeHTML(comic.slug)}/index.html" aria-label="Read ${escapeHTML(comic.title)}">
          <img src="${escapeHTML(comic.cover)}" alt="" loading="lazy">
        </a>
        <div class="card-copy">
          <div class="card-meta">
            <span>${escapeHTML(comic.lessonLabel)}</span>
            <span>${escapeHTML(comic.readTime)}</span>
          </div>
          <h2 lang="fr"><a href="${escapeHTML(comic.slug)}/index.html">${escapeHTML(comic.title)}</a></h2>
          <p>${escapeHTML(comic.summary)}</p>
          <div class="lesson-row" aria-label="French Starter lessons used">
            <span>Lessons</span>
            <strong>${escapeHTML(lessonList)}</strong>
          </div>
          <a class="read-link" href="${escapeHTML(comic.slug)}/index.html">Read the comic <span aria-hidden="true">→</span></a>
        </div>
      </article>
    `;
  }).join("");

  function escapeHTML(value) {
    return String(value)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }
})();
