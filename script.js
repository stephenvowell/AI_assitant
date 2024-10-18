document.addEventListener('DOMContentLoaded', () => {
    fetch('data.json')
        .then(response => response.json())
        .then(data => {
            const newsContainer = document.getElementById('news-container');
            data.forEach(item => {
                const newsItem = document.createElement('div');
                newsItem.className = 'news-item';

                const newsTitle = document.createElement('a');
                newsTitle.className = 'news-title';
                newsTitle.href = item.url;
                newsTitle.textContent = item.title;
                newsTitle.target = '_blank';

                const newsUrl = document.createElement('div');
                newsUrl.className = 'news-url';
                newsUrl.textContent = item.url;

                newsItem.appendChild(newsTitle);
                newsItem.appendChild(newsUrl);
                newsContainer.appendChild(newsItem);
            });
        })
        .catch(error => console.error('Error fetching data:', error));
});