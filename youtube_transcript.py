#  get youtube transcript from the video url
#  using youtube_transcript_api

from youtube_transcript_api import YouTubeTranscriptApi
# english - en, hindi - hi, telugu - te, tamil - ta, kannada - kn, malayalam - ml
# Function to download transcript
def download_transcript(video_id, language='te'):
    try:
        # Get the transcript for the given video ID and language
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
        
        # Save the transcript to a text file
        with open(f"{video_id}_transcript.txt", "w", encoding="utf-8") as file:
            for entry in transcript:
                file.write(f"{entry['text']}\n")
        
        print(f"Transcript downloaded and saved as {video_id}_transcript.txt")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
video_id = 'T2t7K_VJjpc'  # Replace with your YouTube video ID
download_transcript(video_id)
