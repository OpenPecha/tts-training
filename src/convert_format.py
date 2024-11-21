import pandas as pd
import os
import shutil
import requests

df = pd.read_parquet('./data/input/train-00001-of-00005.parquet')

output_dir = './data/output_data'
wav_dir = os.path.join(output_dir, 'wav')
os.makedirs(wav_dir, exist_ok=True)

metadata = []

for _, row in df.iterrows():
    file_name = row['file_name']  
    text = row['uni'] 
    audio_url = row['url'] 

    # Define a new ID for the audio
    audio_id = os.path.splitext(os.path.basename(audio_url))[0]
    target_wav_path = os.path.join(wav_dir, f"{audio_id}.wav")

    # Download the audio file if it's a URL
    if audio_url.startswith('http'):
        response = requests.get(audio_url, stream=True)
        with open(target_wav_path, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
    else:
        # If the audio file is local, just copy it
        shutil.copy(audio_url, target_wav_path)

    metadata.append(f"{audio_id}|{text}")

with open(os.path.join(output_dir, 'train-00001-of-00005.csv'), 'w') as f:
    for line in metadata:
        f.write(line + "\n")

print("Dataset converted to Piper format and saved in", output_dir)

