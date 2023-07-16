# TODO: all BASH and GIT commands.
# TODO: GIT COMMANDS written here
# git clone '---.git'
 
 
 
# write the template.py file



# BASH
# git add .
# git commit -m "folder structure added"
# git push origin main/master (myOrigin here as remote is added at that origin) (git push remote-name branch-name)
# git remote -v (get info of remotes using this line)
# you can come to some branch by following line
# git fetch remote-name
# git checkout remote-name
# git branch --all
# git checkout branch-name
# if you had some changes on repository remotely then pull them first and merge using following line.
# git pull myOrigin master (git pull remote-name branch-name)


# TODO
# create virtual environment for internal project in git bash (conda installment is prerequisite)
# BASH
# conda create -n textSummarization python=3.8 -y
# conda activate textSummarization
 
 
# TODO
# Install hugging face transformer from its website.


 
# write requirements.txt file
# transformers    # hugging face api
# sacrebleu is library which provides row matrix facility used for text summarization
# torch can be installed for GPU version of your machine from pytorch website. but since our machine is running on CPU, we will keep it simple.
# -e .   This will install the new file 'setup.py' in our current working directory.
# 





# write setup.py.



# now you can install the requirements. Make sure you have -e . in your requirements.txt.



# TODO
# BASH
# pip install -r requirements.txt

# ------------------------------------------------------------------------------------------


# BASH
# git add .
# git commit -m "requirements added and Installation done. Project is now setup"
# git push myOrigin master




# write logging exceptions and utils model


# write in logging file
# src --> textSummarizer --> logging -- __init__.py
# you can run main.py to check how logging is taking place via 2 handlers (file creation for logging, terminal itself)
# write main.py
# from textSummarizer.logging import logger
# logger.info("Welcome to custom logging.")
# TODO
# BASH
# conda activate textSummarizer
# python main.py


# TODO
# Set vscode environment to textSummarizer. (logging)







# write utils --> common.py for Box logging.
# a python function used frequently in your code. Say readYAML() for reading YAML file. If this utility function is used in some file again and again, put this function in utils --> common.py. It can be imported as a module.
# ConfigBox file as output because of easy use of dictionary dict.key instead of dict['key]
# ensure_annotations decorator used because input datatype will be strictly needed as int for a function if specified. (check research --> trials.ipynb)








# try everything on Jupyter colab notebook for accessing GPU.
# Text_Summarization.ipynb
# Build model and predict
# train model
# save model
# save tokenizer and load
# predict it
# save ipynb file into research folder






# 1. data ingestion to download na dunzip data.
# then implement data ingestion components
# ingest a data
# downloaded dataset from a link on github.
# https://github.com/ChaitaliKPatil/NLP_Text_Summarizer_Project/raw/master/datasets/samsumdata.zip
# try with notebook experiment in vscode.
# 01_data_ingestion.ipynb
# follow workflow steps mentioned in README file in this ipynb
# you will need to update config.yaml file for creating data ingestion related configuration. Which saves and provides path or URL to use it later on.
# return to 01_data_ingestion.ipynb
# TODO: understand decorators.
# You need to convert it to the modular coding once you have run it on Jupyter.
# Again restart from 1. from the WORKFLOW steps.
# 1,2 is already done.
# 1. Update config.yaml
# 2. Update params.yaml
# skipping to 3rd step.
# step 3. update entity. copy the entity in ingestion notebook. paste in entity-->__init__.py
# step 4. Update the configuration manager in src config. paste in src-->config-->configuration.py
# step 5. update components. paste in src-->components--> data_ingestion.py
# step 6. update the pipeline. paste in src-->pipeline--> stage_01_data_ingestion.py
# step 7. update the main.py in order to run this.
# delete artifacts folder first to check if it gets created again after running main.py
# 
# MAIN.PY 2:01:55/3:38:03
# It ran successfully. 
# TODO: GIT COMMIT without artifacts. so mention .gitignore file.
# write "artifacts/*" in .gitignore so that this folder wont be committed ever to github.
# 
# BASH
# Git Commit and push to github
# git commit -m "data ingestion notebook added"








# 2. data validation if we have correct datasets available to us.
# 02_data_validation.ipynb (research)
# MAIN.PY run successfully
# BASH
# Git Commit and push to github
# git commit -m "data validation notebook added"







# 3. data transformation to convert data into features. which we did in Text_Summarization.ipynb
# 03_data_transformation.ipynb (research)
# MAIN.PY run successfully
# BASH
# Git Commit and push to github
# git commit -m "data transformation notebook added"





# TRAINING MODEL ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------

# 4. model_trainer for training model.
# 04_model_trainer.ipynb (research)
# WORKFLOW 
# step 2. update params.yaml .These parameters are needed when we train model. in Text_Summarization.ipynb we hardcoded parameters using TrainingArguments module. We can change them in params.yaml.
# write params.yaml
# MAIN.PY run successfully
# BASH







# 5. model evaluation for checking with the help og metric we wrote in TextSummarization.ipynb
# 05_model_evaluation.ipynb (research). Run it.
# Git Commit and push to github
# git commit -m "model evaluation completed successfully"
# git push myOrigin master







# prediction pipeline to be written which we wrote in TextSummarization.ipynb
# prediction.py (research)
# last cell of prediction in TextSummarization.ipynb.
# we need to link this to web application.
# so write app.py to create web application






# step 8. update the app.py
# so write app.py to create web application
# give 2 routs in app.py 1. for training, 2. for prediction output to show on UI.
# start port nd host.
# 
# TODO: run app.py on bash
# BASH
# python app.py
# while this command runs, open google browser and type "localhost:8080"
# it will start "localhost:8080/docs"
# you can click button to "Try it out"/execute training which will take lot of time.
# once successful!, you can predict "Try it out". Enter some text/dialogue for prediction.
# hurray!!!!!!!! Time for Deployment.












# DEPLOY MODEL --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# we need to integrate with Docker. 
# Service used: Elastic Container Study. Its from AWS
# It will create a Docker image of source code.
# Then it will push the Docker image to the Elastic Container Study.
# From Elastic Container Study, we will pull images and run those images into our EC2 instance.
# This is CI/CD deployment which will directly get deployed from the github repository.
# CI/CD tool used: GitHub action.
# 
# 
# Write Docker file.
# Thus simple Docker image is created.
# 
# 
# For CI/CD deployment, create one file under folder ".github\workflows"
# "main.yaml"
# 
# 
# 
# 
# AWS Deployment
# login to console
# textSummary(username), text-summary (ECR name), textSummary-machine, textkeypair,
# IAM user to be created (Identity Access Management)
# key-pair (textkeypair.pem) .pem file can be used when you will run this service from your local computer using SuperPutty.
# 
# 
# 
# 
# BASH Git commit.
# git add .
# git commit -m "ci/cd added"
# it was getting deployed on AWS through github already.
# http://16.16.104.222:8080/docs
