/**
 * Infographic Component
 * Generates the HTML for the news card based on the data object.
 */
const Infographic = {
  // Icon mapping for categories
  icons: {
    product: "fa-rocket",
    business: "fa-building",
    research: "fa-flask",
    policy: "fa-gavel",
    hack: "fa-code",
  },

  // Category display names
  categoryNames: {
    product: "Product & Service",
    business: "Business Case",
    research: "Research & Tech",
    policy: "Policy & Governance",
    hack: "Hacks & Tips",
  },

  /**
   * Create the card HTML string
   * @param {Object} item - The news item object
   * @returns {string} HTML string
   */
  createCard: function (item) {
    const iconClass = this.icons[item.category] || "fa-newspaper";
    const categoryName = this.categoryNames[item.category] || item.category;

    // Generate metrics HTML
    let metricsHtml = "";
    if (item.metrics && item.metrics.length > 0) {
      metricsHtml = '<div class="metrics-container">';
      item.metrics.slice(0, 3).forEach((metric) => {
        metricsHtml += `
                    <div class="metric-badge">
                        <span class="metric-label">${metric.label}</span>
                        <span class="metric-value">${metric.value}</span>
                    </div>
                `;
      });
      metricsHtml += "</div>";
    }

    // Generate tags HTML
    let tagsHtml = "";
    if (item.tech_tags) {
      tagsHtml += '<div class="tags">';
      item.tech_tags.slice(0, 3).forEach((tag) => {
        tagsHtml += `<span class="tag">#${tag}</span>`;
      });
      tagsHtml += "</div>";
    }

    return `
            <article class="card" onclick="window.location.href='detail.html?id=${item.id}'">
                <div class="card-header">
                    <div class="category-icon">
                        <i class="fas ${iconClass}"></i>
                    </div>
                    <span class="date">${item.date}</span>
                </div>
                <h2 class="card-title">${item.title_ja}</h2>
                <p class="card-summary">${item.summary_short_ja}</p>
                ${metricsHtml}
                ${tagsHtml}
            </article>
        `;
  },

  /**
   * Render the detail view HTML
   * @param {Object} item - The news item object
   * @returns {string} HTML string
   */
  renderDetail: function (item) {
    const iconClass = this.icons[item.category] || "fa-newspaper";
    const categoryName = this.categoryNames[item.category] || item.category;

    // Key points HTML
    let keyPointsHtml = "";
    if (item.key_points && item.key_points.length > 0) {
      keyPointsHtml = `
                <div class="key-points">
                    <h3><i class="fas fa-check-circle" style="color: var(--accent-secondary); margin-right: 10px;"></i>Key Points</h3>
                    <ul>
                        ${item.key_points
                          .map((point) => `<li>${point}</li>`)
                          .join("")}
                    </ul>
                </div>
            `;
    }

    // Sources HTML
    let sourcesHtml = "";
    if (item.sources && item.sources.length > 0) {
      sourcesHtml = `
                <div class="sources-section">
                    <h3>Sources</h3>
                    ${item.sources
                      .map(
                        (source) => `
                        <a href="${source.url}" target="_blank" class="source-link">
                            <div style="display: flex; justify-content: space-between;">
                                <strong>${source.media}</strong>
                                <span style="font-family: var(--font-mono); font-size: 0.8rem;">${source.date}</span>
                            </div>
                            <div>${source.title}</div>
                        </a>
                    `
                      )
                      .join("")}
                </div>
            `;
    }

    return `
            <div class="detail-header">
                <div class="detail-meta">
                    <span><i class="fas ${iconClass}"></i> ${categoryName}</span>
                    <span>|</span>
                    <span>${item.date}</span>
                </div>
                <h1 class="detail-title">${item.title_ja}</h1>
                
                <!-- Re-use metrics for detail view but larger -->
                <div class="metrics-container" style="margin-bottom: 2rem; justify-content: flex-start;">
                    ${
                      item.metrics
                        ? item.metrics
                            .map(
                              (metric) => `
                        <div class="metric-badge" style="flex: 0 0 auto; min-width: 120px;">
                            <span class="metric-label">${metric.label}</span>
                            <span class="metric-value" style="font-size: 1.2rem;">${metric.value}</span>
                        </div>
                    `
                            )
                            .join("")
                        : ""
                    }
                </div>
            </div>

            <div class="detail-content">
                <p style="font-size: 1.2rem; margin-bottom: 2rem; color: var(--text-primary);">${
                  item.summary_short_ja
                }</p>
                ${keyPointsHtml}
                <div class="long-summary">
                    ${item.summary_long_ja.replace(/\n/g, "<br>")}
                </div>
                ${sourcesHtml}
            </div>
        `;
  },
};
