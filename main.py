from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Movie(BaseModel):
    id: int
    title: str
    release_year: int

class Celebrity(BaseModel):
    id: int
    name: str
    birth_year: int

class NewsArticle(BaseModel):
    id: int
    title: str
    content: str
    published_at: str

movies = [
    Movie(id=1, title="Movie 1", release_year=2020),
    Movie(id=2, title="Movie 2", release_year=2021),
    Movie(id=3, title="Movie 3", release_year=2022)
]

celebrities = [
    Celebrity(id=1, name="Celebrity 1", birth_year=1980),
    Celebrity(id=2, name="Celebrity 2", birth_year=1990),
    Celebrity(id=3, name="Celebrity 3", birth_year=2000)
]

news_articles = [
    NewsArticle(id=1, title="News Article 1", content="This is news article 1", published_at="2022-01-01"),
    NewsArticle(id=2, title="News Article 2", content="This is news article 2", published_at="2022-01-02"),
    NewsArticle(id=3, title="News Article 3", content="This is news article 3", published_at="2022-01-03")
]

@app.get("/movies/")
def read_movies():
    return movies

@app.get("/celebrities/")
def read_celebrities():
    return celebrities

@app.get("/news/")
def read_news():
    return news_articles

@app.get("/movies/{movie_id}")
def read_movie(movie_id: int):
    for movie in movies:
        if movie.id == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")

@app.get("/celebrities/{celebrity_id}")
def read_celebrity(celebrity_id: int):
    for celebrity in celebrities:
        if celebrity.id == celebrity_id:
            return celebrity
    raise HTTPException(status_code=404, detail="Celebrity not found")

@app.get("/news/{news_id}")
def read_news_article(news_id: int):
    for news_article in news_articles:
        if news_article.id == news_id:
            return news_article
    raise HTTPException(status_code=404, detail="News article not found")
```
**Database (SQLite)**