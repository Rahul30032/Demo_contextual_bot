<!-- #### This file contains tests to evaluate that your bot behaves as expected.
#### If you want to learn more, please see the docs: https://rasa.com/docs/rasa/user-guide/testing-your-assistant/

## happy path 1
* greet: hello there!
  - utter_greet
* mood_great: amazing
  - utter_happy

## happy path 2
* greet: hello there!
  - utter_greet
* mood_great: amazing
  - utter_happy
* goodbye: bye-bye!
  - utter_goodbye

## sad path 1
* greet: hello
  - utter_greet
* mood_unhappy: not good
  - utter_cheer_up
  - utter_did_that_help
* affirm: yes
  - utter_happy

## sad path 2
* greet: hello
  - utter_greet
* mood_unhappy: not good
  - utter_cheer_up
  - utter_did_that_help
* deny: not really
  - utter_goodbye

## sad path 3
* greet: hi
  - utter_greet
* mood_unhappy: very terrible
  - utter_cheer_up
  - utter_did_that_help
* deny: no
  - utter_goodbye

## say goodbye
* goodbye: bye-bye!
  - utter_goodbye

## bot challenge
* bot_challenge: are you a bot?
  - utter_iamabot
 -->

## greet + goodbye
* greet: Hi!
  - utter_greet
* bye: Bye
  - utter_bye

## greet + thanks
* greet: Hello there
  - utter_greet
* thank: thanks a bunch
  - utter_noworries

## greet + thanks + goodbye
* greet: Hey
  - utter_greet
* thank: thank you
  - utter_noworries
* bye: bye bye
  - utter_bye


## ask channels
* faq: What messaging channels does Rasa support?
  - respond_faq

## ask languages
* faq: Which languages can I build assistants in?
  - respond_faq

## ask rasa x
* faq: What’s Rasa X?
  - respond_faq