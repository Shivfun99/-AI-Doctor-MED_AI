import os
import platform
import subprocess
from gtts import gTTS
from pydub import AudioSegment

def text_to_speech_with_gtts(input_text, output_filepath="output.mp3"):
    language = "en"
    audio = gTTS(text=input_text, lang=language, slow=False)
    audio.save(output_filepath)

    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":
            # Convert MP3 to WAV
            wav_path = output_filepath.replace(".mp3", ".wav")
            sound = AudioSegment.from_mp3(output_filepath)
            sound.export(wav_path, format="wav")

            # Play WAV
            subprocess.run([
                'powershell', 
                '-c', f'(New-Object Media.SoundPlayer "{wav_path}").PlaySync();'
            ])
        elif os_name == "Linux":
            subprocess.run(['aplay', output_filepath])  # or 'mpg123', 'ffplay'
        else:
            raise OSError("Unsupported OS")
    except Exception as e:
        print(f"Error playing audio: {e}")

# Example usage
input_text = "Hi! This is a test using gTTS with WAV autoplay on Windows."
text_to_speech_with_gtts(input_text, output_filepath="gtts_test.mp3")
