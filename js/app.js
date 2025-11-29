/**
 * Main Application Logic
 */
document.addEventListener('DOMContentLoaded', async () => {
    const gridContainer = document.getElementById('news-grid');
    const detailContainer = document.getElementById('detail-content');

    try {
        console.log("Fetching news data from data/news.json...");
        // Fetch data
        const response = await fetch('data/news.json');
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log("Data loaded successfully:", data);
        const newsItems = data.items;

        // Check if we are on the detail page
        const urlParams = new URLSearchParams(window.location.search);
        const detailId = urlParams.get('id');

        if (detailId && detailContainer) {
            console.log("Rendering detail view for ID:", detailId);
            // Render Detail View
            const item = newsItems.find(i => i.id === detailId);
            if (item) {
                detailContainer.innerHTML = Infographic.renderDetail(item);
            } else {
                console.error("Article not found for ID:", detailId);
                detailContainer.innerHTML = '<p>Article not found.</p>';
            }
        } else if (gridContainer) {
            console.log("Rendering grid view with items:", newsItems.length);
            // Render Grid View
            gridContainer.innerHTML = newsItems.map(item => Infographic.createCard(item)).join('');
        }

    } catch (error) {
        console.error('Error loading data:', error);
        let errorMsg = `<div style="text-align:center; color: #ff4d4d; padding: 2rem;">
            <i class="fas fa-exclamation-triangle fa-2x"></i>
            <p style="margin-top: 1rem; font-weight: bold;">Failed to load intelligence stream.</p>
            <p style="font-size: 0.9rem; opacity: 0.8;">${error.message}</p>
        </div>`;
        
        // Specific advice for file:// protocol (CORS)
        if (window.location.protocol === 'file:') {
            errorMsg += `<div style="text-align:center; color: #a0a8c0; margin-top: 1rem; font-size: 0.9rem;">
                <p><strong>Note:</strong> Browsers often block loading JSON files directly from the disk (CORS).</p>
                <p>Please run a local server:</p>
                <code style="background:rgba(255,255,255,0.1); padding:0.2rem 0.5rem; border-radius:4px;">python3 -m http.server</code>
                <p>Then open <a href="http://localhost:8000" style="color:#00f2ff;">http://localhost:8000</a></p>
            </div>`;
        }

        if (gridContainer) gridContainer.innerHTML = errorMsg;
        if (detailContainer) detailContainer.innerHTML = errorMsg;
    }
});
