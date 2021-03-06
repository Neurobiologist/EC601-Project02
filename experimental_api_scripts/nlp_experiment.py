#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NLP Test

@author: MeganParsons
"""
# Import Google Client Library and Instantiate a Client
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
client = language.LanguageServiceClient()

# Prepare text
tweet = "They were the most vulnerable to COVID — thousands of elders in nursing homes across the state. Yet for the Baker administration, praised for its overall pandemic response, they were for too long a secondary priority. The result was calamity: 1 in 7 dead."
document = language.types.Document(
  content=tweet, 
  type=enums.Document.Type.PLAIN_TEXT)

# Sentiment Analysis
response = client.analyze_sentiment(
  document=document,
  encoding_type='UTF32',
  )

sentiment = response.document_sentiment

print('Sentiment Score:', sentiment.score)
print('Sentiment Magnitude:',sentiment.magnitude)

# Analyze Entities
response2 = client.analyze_entities(
     document=document,
     encoding_type='UTF32',
 )

# Use this code from the API documentation to validate results from analyze_entities
for entity in response2.entities:
  print('=' * 20)
  print('         name: {0}'.format(entity.name))
  print('         type: {0}'.format(entity.type))
  print('     metadata: {0}'.format(entity.metadata))
  print('     salience: {0}'.format(entity.salience))
