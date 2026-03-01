import os
import re

base_dir = r"c:\Saft Family Files\The Heritage Letters"
stories = {
    1: {"name": "Evelyn Vance", "quote": "The world is always ending for someone, and it's always beginning for someone else. The trick is to find the melody connecting the two.", "author": "Evelyn Vance", "book": "The Sound of the City", "reason": "It captures the exact rhythm of Chicago in the 50s.", "music": "Ella Fitzgerald, Duke Ellington", "movie": "Casablanca"},
    2: {"name": "Arthur Pendelton", "quote": "People today are too quick to throw things away when they stop working... the repaired bond is often stronger than the original cast.", "author": "Arthur Pendelton", "book": "The Toaster Project", "reason": "A fascinating look at what it actually takes to build something from scratch.", "music": "Glenn Miller, Big Band Swing", "movie": "The Great Escape"},
    3: {"name": "Maria Gonzalez", "quote": "Home isn't a coordinate on a map. Home is the space you create between the people who love you.", "author": "Maria Gonzalez", "book": "One Hundred Years of Solitude", "reason": "It perfectly understands the magic and chaos of Latin American family life.", "music": "Celia Cruz, Buena Vista Social Club", "movie": "Cinema Paradiso"},
    4: {"name": "James 'Doc' Harrison", "quote": "Medicine today treats the body like a complex machine... But a patient is a story, not a machine. If you ignore the narrative, you miss the disease.", "author": "James Harrison", "book": "The Tennis Partner", "reason": "A profound look at the vulnerabilities even doctors face.", "music": "Johnny Cash, Classic Country", "movie": "To Kill a Mockingbird"},
    5: {"name": "Yoko Tanaka", "quote": "The masterpiece is not the ink on the paper; the masterpiece is the calm mind you earn in the process.", "author": "Yoko Tanaka", "book": "The Book of Tea", "reason": "The quintessential explanation of finding beauty in imperfection and simplicity.", "music": "Traditional Koto Music, Yo-Yo Ma", "movie": "Seven Samurai"},
    6: {"name": "Silas Montgomery", "quote": "Courage is not the absence of terror. It is the decision that your dignity is more valuable than your physical safety.", "author": "Silas Montgomery", "book": "The Fire Next Time", "reason": "Required reading for anyone trying to understand the soul of America.", "music": "Sam Cooke, Aretha Franklin", "movie": "In the Heat of the Night"},
    7: {"name": "Eleanor Hughes", "quote": "You cannot apologize for taking up space. If you are competent, you belong in the room. Make them deal with your reality.", "author": "Eleanor Hughes", "book": "Slouching Towards Bethlehem", "reason": "Joan Didion's sharp, unsentimental observation is how I tried to edit.", "music": "Frank Sinatra, Cole Porter", "movie": "All About Eve"},
    8: {"name": "Mateo Rivera", "quote": "When the storm is breaking over the bow, praying won't save you. Fastening the hatch will save you. Panic is a luxury you cannot afford.", "author": "Mateo Rivera", "book": "The Old Man and the Sea", "reason": "No book captures the respect and sheer terror of the ocean more perfectly.", "music": "Salsa, Héctor Lavoe", "movie": "Jaws (but he hates how inaccurate the fishing is)"},
    9: {"name": "Iris Johansen", "quote": "The greatest mistake we make with both plants and people is trying to force them to conform to our schedule.", "author": "Iris Johansen", "book": "The Orchid Thief", "reason": "A wildly entertaining, although slightly exaggerated, look into the obsessive world of flower collecting.", "music": "Classical Piano, Chopin", "movie": "Adaptation"},
    10: {"name": "Thomas Keller", "quote": "The defining characteristic of an adult isn't that you never fail. It's that when the floor drops out from under you, you figure out how to build a ladder.", "author": "Thomas Keller", "book": "Working", "reason": "Studs Terkel understood better than anyone that our jobs define our dignity.", "music": "Motown, The Temptations", "movie": "Rocky"}
}

def inject_favorites():
    for num, data in stories.items():
        path = os.path.join(base_dir, f"story-{num}.html")
        if not os.path.exists(path):
            continue
            
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        favorites_html = f"""
            <hr style="margin: var(--spacing-lg) 0; border: 0; border-top: 1px solid var(--color-border);">
            
            <section class="favorites-section" style="background: var(--color-white); padding: var(--spacing-md); border-radius: var(--radius-md); box-shadow: 0 4px 6px rgba(0,0,0,0.02); border: 1px solid var(--color-border);">
                <h3 style="color: var(--color-accent); font-family: var(--font-heading); margin-bottom: var(--spacing-md); border-bottom: 2px solid var(--color-border); padding-bottom: 0.5rem;">Favorites & Recommendations</h3>
                
                <div style="margin-bottom: 1.5rem;">
                    <h4 style="font-family: var(--font-ui); font-size: 1rem; color: var(--color-text-light); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem;">Favorite Quote</h4>
                    <p style="font-style: italic; font-size: 1.1rem; margin-bottom: 0;">"{data['quote']}"</p>
                    <p style="text-align: right; font-size: 0.9rem; color: var(--color-text-light); margin-top: 0.5rem;">— {data['author']}</p>
                </div>

                <div style="margin-bottom: 1.5rem;">
                    <h4 style="font-family: var(--font-ui); font-size: 1rem; color: var(--color-text-light); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem;">Recommended Reading</h4>
                    <p style="font-weight: bold; margin-bottom: 0.2rem;"><a href="https://www.amazon.com/s?k={data['book'].replace(' ', '+')}&tag=YOUR_AFFILIATE_TAG" target="_blank" rel="noopener noreferrer">{data['book']}</a></p>
                    <p style="font-size: 0.95rem;">{data['reason']}</p>
                </div>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                    <div>
                        <h4 style="font-family: var(--font-ui); font-size: 1rem; color: var(--color-text-light); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem;">Music</h4>
                        <p style="font-size: 0.95rem;">{data['music']}</p>
                    </div>
                    <div>
                        <h4 style="font-family: var(--font-ui); font-size: 1rem; color: var(--color-text-light); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem;">Movies</h4>
                        <p style="font-size: 0.95rem;">{data['movie']}</p>
                    </div>
                </div>
            </section>
        """
        
        # Inject right before the closing </article> tag
        if "Favorites & Recommendations" not in content:
            content = content.replace("</article>", f"{favorites_html}\n        </article>")
            
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

inject_favorites()
print("Favorites injected into all story profiles.")
