import scrapy

class InfoSpider(scrapy.Spider):
    name = "my_spider"

    def start_requests(self):
        # Lire les URLs à partir du fichier urls_muzeo.txt
        with open('urls_muzeo.txt', 'r') as file:
            urls = file.readlines()
        
        # Parcourir chaque URL pour créer une requête
        for url in urls:
            yield scrapy.Request(url.strip(), callback=self.parse_muzeo_page)

    def parse_muzeo_page(self, response):

        # Extraction des informations
        titre = response.css('span.title_oeuvre::text').get()
        prix = response.css('.prix_livraison strong::text').get()
        delai_fabrication = response.css('.delai_fabrication strong::text').get()
        url_image = response.css('#papier_peint_mes_img::attr(style)').re_first(r"url\('([^']+)'\)")

        # Stockage des informations dans un modèle de données ou autre
        yield {
            'titre': titre,
            'prix': prix,
            'delai_fabrication': delai_fabrication,
            'url_image': url_image,
        }