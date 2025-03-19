
##Model Training and Deployment Process  

The Tibetan Text-to-Speech (TTS) model was trained following the guidelines provided in the [AI4Bharat](https://github.com/AI4Bharat/Indic-TTS). I initially experimented with an existing Hindi TTS model to familiarize myself with the training pipeline and workflow. This provided a clearer understanding of how the training process operates, including data preprocessing, model configuration, and inference generation.  


## Comparative Performance: Hindi vs. Tibetan Model  

During experimentation, it became evident that the Hindi model performed better than the Tibetan model. This is because of several reasons:  
- The availability of high-quality training data for Hindi, whereas Tibetan TTS suffers from a lack of extensive datasets. 
- Hindi has pre-existing phoneme support in AI4Bharat’s framework, whereas Tibetan required additional adjustments.  


##Configuration Adjustments for the Tibetan Model  

To adapt the model for Tibetan, several key modifications were made to the configuration files:  
- Phoneme Language Setting:  
The phoneme language was initially set as "bo" (Tibetan, as per ISO 639-1).  
However, the AI4Bharat framework did not recognize "bo" as a standard phoneme set.  
To circumvent this issue, "en" (English) was set as the fallback language to ensure compatibility.  
- Wylie Transliteration Integration:  
Since "bo" was not directly supported, Wylie transliteration was incorporated as an intermediary representation.  
This helped in maintaining phonetic accuracy while mapping Tibetan characters to a format that the model could process effectively.  


##Training Process  

- Once the configurations were finalized, model training was initiated on Vast.ai, a cloud-based GPU platform. The FastPitch model was trained for 2500 epochs, and the training process took approximately eight days. 
- Throughout the training process, model performance metrics, loss curves, and other relevant statistics were tracked and visualized using Weights & Biases (WandB). These logs provided real-time insights into model progression and helped in debugging potential issues.  


## Inference and Audio Generation

- After successful training, the trained model was tested by running inference. The model was able to generate Tibetan speech from input text, validating that the training process had been effective.  
- To make the model more accessible, a Gradio-based API was developed for local testing. A simple script was written to host the model via a web-based interface, allowing a user to interact with it easily.  


## Deployment via Gradio API  

- The Gradio interface consists of a basic input-output system, where users can enter Tibetan text in the input field.  
- Upon submitting the text, the model processes it and generates the corresponding speech output.  
- The resulting Tibetan speech audio is played back to the user, demonstrating the successful application of the trained model. 



 <img width="1440" alt="screenshot1" src="https://github.com/user-attachments/assets/c0aaa1b1-88dc-45cf-a3bd-e6448da03178" />




##Challenges Faced During Training

The training process encountered multiple challenges, primarily due to initial errors in phoneme handling and dataset limitations:
- Phoneme Recognition Issues: The model did not recognize "bo" as a valid phoneme language, requiring the use of "en" as a fallback. This caused some inconsistencies in pronunciation, necessitating additional tweaks to Wylie's transliteration.
- Dataset Limitations: The lack of a large-scale Tibetan speech dataset affected model performance, leading to higher loss values and slower convergence compared to the Hindi model.
Training Stability Issues: During the early training stages, issues with learning rate configuration and memory constraints on Vast.ai GPUs led to interruptions, requiring adjustments.

Despite these difficulties, the model was successfully trained, and key insights were gained that could help improve future iterations of Tibetan TTS systems.
