# Joke FastAPI app

- A simple web API for serving jokes!

### URLS:

- `/joke`:
  - `programming` (optional bool paramter) if you want programming jokes
    - Eg: `/joke?programming=True`
    ```json
    {
        "category": "Programming",
        "id": "52dc7dee-5a24-4121-bfe4-0f047c8403c7",
        "joke": "There are 10 types of people in this world...\nThose who understand binary and those who don't"
    }
    ```
    - Eg: `/joke`
    ```json
    {
      "category": "dad",
      "id": "mbpbapbhiyd",
      "joke": "Did you hear about the bread factory burning down? They say the business is toast."
    }
    ```

- `/docs`
  - For documentation of all routes
  
- `/`
  - Health check to ensure system is up and running!

### Deployment link:

[Vercel](https://give-me-joke.vercel.app/joke)

### Deploy your own:

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fc2p-cmd%2Fgive_me_joke)

### Running locally:

**Clone**:
```shell
git clone https://github.com/c2p-cmd/give_me_joke.git
cd give_me_joke
```

**Create venv**:
```shell
python3 venv -m venv
source venv/bin/activate
pip3 install -r requirements.txt
```

**Run app**
```shell
uvicorn server.app:app --host 0.0.0.0 --port 7860 --reload
```

**Open `http://localhost:7860` in browser!**