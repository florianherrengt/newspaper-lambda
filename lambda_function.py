from newspaper import Article

def lambda_handler(event, context):
    url = event['params']['querystring']['url']
    article = Article(url)
    article.download()
    article.parse()

    return {
        'url': article.url,
        'title': article.title,
        'top_image': article.top_img,
        'images': [x for x in article.imgs],
        'text': article.text,
        'keywords': article.keywords,
        'authors': article.authors,
        'summary': article.authors,
        'authors': article.authors,
        'meta_description': article.meta_description,
        'meta_lang': article.meta_lang,
        'meta_favicon': article.meta_favicon,
        'meta_keywords': article.meta_keywords,
        'canonical_link': article.canonical_link,
        'tags': [unicode(x) for x in article.tags],
        'movies': article.movies,
        'additional_data': article.additional_data,
    }
