#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module provides two functions for translating text between English and
French using the IBM Watson Language Translator.

The module includes the following functions:

- watson_authenticate(): Returns a configured instance of the IBM Watson
Language Translator.
- english_to_french(english_text: str) -> str: Translates English text to
French using IBM Watson Language Translator.
- french_to_english(french_text: str) -> str: Translates French text to
English using IBM Watson Language Translator.

The module requires that the following environment variables be set:

- version: The version of the IBM Watson Language Translator to use.
- apikey: The API key for accessing the IBM Watson Language Translator.
- url: The URL of the IBM Watson Language Translator service.

If any of these environment variables are not set, an error will be raised.

Example usage:

    # Translate English text to French
    french_text = english_to_french('Hello, how are you?')
    print(french_text)  # Bonjour comment ça va?

    # Translate French text to English
    english_text = french_to_english('Bonjour, comment ça va?')
    print(english_text)  # Hello, how are you?
"""

import os
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3

load_dotenv()

def watson_authenticate():
    """
    Returns a configured instance of the IBM Watson Language Translator.

    This function reads the IBM Watson credentials from the environment variables and uses them to
    create and return an authenticated instance of the IBM Watson Language Translator.

    Returns:
        LanguageTranslatorV3: An instance of the IBM Watson Language Translator.
    """
    version = os.environ['version']
    apikey = os.environ['apikey']
    url = os.environ['url']

    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version=version,
        authenticator=authenticator
    )
    language_translator.set_service_url(url)

    return language_translator


def english_to_french(english_text):
    """
    Translates English text to French using IBM Watson Language Translator.

    This function takes English text as input and uses IBM Watson Language Translator to translate
    it to French.

    Args:
        english_text (str): The English text to be translated.

    Returns:
        str: The French translation of the input text, or None if the input is None.
    """
    if english_text is not None:
        language_translator = watson_authenticate()
        translation = language_translator.translate(
            text=english_text,
            model_id='en-fr'
        ).get_result()
        french_text = translation["translations"][0]["translation"]

        return french_text
    return None

def french_to_english(french_text):
    """
    Translates French text to English using IBM Watson Language Translator.

    This function takes French text as input and uses IBM Watson Language Translator to translate
    it to English.

    Args:
        french_text (str): The French text to be translated.

    Returns:
        str: The English translation of the input text, or None if the input is None.
    """
    if french_text is not None:
        language_translator = watson_authenticate()
        translation = language_translator.translate(
            text=french_text,
            model_id='fr-en'
        ).get_result()
        english_text = translation["translations"][0]["translation"]

        return english_text
    return None

