# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

from rasa_core_sdk import Action
from rasa_sdk.events import UserUtteranceReverted
# from rasa_core_sdk.events import SlotSet


class SalesForm(FormAction):
    """Collects sales information and adds it to the spreadsheet"""

    def name(self) -> Text:
        return "sales_form"

    @staticmethod
    def required_slots(tracker) -> List[Text] :
        return ["job_function","use_case","budget","person_name","company","business_email"]
	
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
        """A dictionary to map required slots to
    - an extracted entity
    - intent: value pairs
    - a whole message
    or a list of them, where a first match will be picked"""
        return {
        "use_case": self.from_text(intent="inform"),
        "company" : self.from_text(intent="inform") ,
        "job_function" : self.from_text(intent="inform") ,
        "person_name" : [self.from_text(intent="inform"), self.from_entity(entity = "person_name" , intent="inform")] ,
        "budget": self.from_text(intent="inform") ,
        "business_email": self.from_text(intent="inform") ,
        }
		
    def submit(
	        self,
	        dispatcher: CollectingDispatcher,
	        tracker: Tracker,
	        domain: Dict[Text, Any],
	    ) -> List[Dict]:

        dispatcher.utter_message("Thanks for getting in touch, we’ll contact you soon")
        return []


class ActiongreetUser(Action):
    def name(self):
        return "action_greet"

    def run(self,dispatcher,tracker,domain):
        dispatcher.utter_template("utter_greet",tracker)
        return [UserUtteranceReverted()]