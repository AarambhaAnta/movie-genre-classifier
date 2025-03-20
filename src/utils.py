from model import load_model, load_vectorizer, predict_genre

# Define paths
MODEL_PATH = "./models/saved_models/linearsvc_best.pkl"
VECTORIZER_PATH = "./models/saved_models/tfidf_vectorizer.pkl"

# Load model and vectorizer
model = load_model(MODEL_PATH)
vectorizer = load_vectorizer(VECTORIZER_PATH)


def main():
    """Ask the user for a movie description and predict its genre."""
    while True:
        movie_desc = input("\nEnter a movie description (or type 'exit' to quit): ").strip()
        
        if movie_desc.lower() == "exit":
            print("Goodbye! 🎬")
            break

        predicted_genre = predict_genre(model, movie_desc, vectorizer)
        print(f"\n🎥 Predicted Genre: {predicted_genre}")

if __name__ == "__main__":
    main()






# def get_genre_from_description(description):
#     """Get the predicted genre for a given movie description."""
#     return predict_genre(model, description, vectorizer)

# # Example Usage
# if __name__ == "__main__":
#     movie_desc = "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival."
#     predicted_genre = get_genre_from_description(movie_desc)
#     print("Predicted Genre:", predicted_genre)
