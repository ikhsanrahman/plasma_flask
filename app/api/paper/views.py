""" this is helper module to assist server to send a message to customer """


import json
import requests
import time
from flask import jsonify

from app.api.create_app import db
from app.api.config import config, wavecell_config
from app.api.errors.errors import Errors
from app.api.db_model import SingleSms, SingleSmsCustom, BatchSms, BatchSmsCustom

SMS_SERVICES = config.Config.SMS_SERVICES
API_SERVICES = wavecell_config
SMS_OTP_ERRORS = Errors.SMS_OTP_ERRORS

class SendMessage :
    """ class for Mobile Sms Verification"""

    def __init__ (self):
        pass

    def postSingletoAPI(self, data) :
        ''' post information to API wavecell for single message'''
        API_NAME = "Single_Sms"
        responses = { }
        headers = {
            "content-type": "application/json"
        }
        headers["Authorization"] = "Bearer {}".format(API_SERVICES.API_KEY)
        log = SingleSms(phone_number=data['destination'],
                        provider=SMS_SERVICES['PROVIDER'],
                        api_name=API_NAME,
                        sms_request=data)
        start_time = time.time()
        db.session.add(log)

        try:
            r = requests.post(
                SMS_SERVICES['SMS_API']["BASIC_API"],
                data=json.dumps(data),
                headers=headers,
            )
            if r.status_code != 200:
                log.set_status_request(dict(r.json()['message']))
                log.save_response_time(time.time() - start_time)
                responses['status_code'] = r.status_code
                responses['message'] = r.json()['message']
                return responses

        except requests.exceptions.Timeout:
            return "REQUEST_TIMEOUT"
        except requests.exceptions.TooManyRedirects:
            return "BAD_URL"
        except requests.exceptions.RequestException as e:
            print(str(e))
            return "FAILURE"
        #end try
        log.save_response_time(time.time() - start_time)
        log.save_response(dict(r.json()))
        log.set_status_request(dict(r.json()['status']))
        db.session.commit()

        responses['message'] = SMS_SERVICES['SUCCESS']
        responses['status'] = r.json()['status']
        responses['status_code'] = r.status_code
        return responses

    #end def


    def postSingle(self, payload) :
        ''' tell to api to send post information '''
        responses = {}
        # build payload

        data = {
            "destination"       : payload['destination'],
            "country"           : API_SERVICES.COUNTRY,
            "text"              : API_SERVICES.TEXT,
            "encoding"          : API_SERVICES.ENCODING,
            "source"            : payload['source']
        }

        result = self.postSingletoAPI(data)
        if result['status_code'] != 200:
            responses["status"] = "FAILED"
            responses["data"  ] = SMS_OTP_ERRORS["FAILURE"]
            responses['status_code'] = result['status_code']
            responses['message'] = result['message']
            return responses
        if result == "REQUEST_TIMEOUT":
            responses["status"] = "FAILED"
            responses['status_code'] = result['status_code']
            responses["data"  ] = SMS_OTP_ERRORS["TIMEOUT"]
            return responses
        if result == "BAD_URL":
            responses["status"] = "FAILED"
            responses['status_code'] = result['status_code']
            responses["data"  ] = SMS_OTP_ERRORS["REDIRECT"]
            return responses
        if result == "EXCEPTION":
            responses["status"] = "FAILED"
            responses['status_code'] = result['status_code']
            responses["data"  ] = SMS_OTP_ERRORS["EXCEPTION"]
            return responses
        #end if
        return result
    #end def

    def postSingleCustomtoAPI(self, data) :
        ''' post information to API wavecell for single message but in custom form'''
        
        API_NAME = "Single_Sms_Custom"
        responses = {}

        headers = {
            "content-type": "application/json"
        }
        headers["Authorization"] = "Bearer {}".format(API_SERVICES.API_KEY)
        log = SingleSmsCustom(phone_number=data['destination'],
                        provider=SMS_SERVICES['PROVIDER'],
                        api_name=API_NAME,
                        sms_request=data)
        start_time = time.time()
        db.session.add(log)

        try:
            r = requests.post(
                SMS_SERVICES['SMS_API']["BASIC_CUSTOM_API"],
                data=json.dumps(data),
                headers=headers,
            )
            if r.status_code != 200:
                log.set_status_request(dict(r.json()['message']))
                log.save_response_time(time.time() - start_time)
                responses['status_code'] = r.status_code
                responses['message'] = r.json()['message']
                return responses

        except requests.exceptions.Timeout:
            return "REQUEST_TIMEOUT"
        except requests.exceptions.TooManyRedirects:
            return "BAD_URL"
        except requests.exceptions.RequestException as e:
            print(str(e))
            return "FAILURE"
        #end try
        log.save_response_time(time.time() - start_time)
        log.save_response(dict(r.json()))
        log.set_status_request(dict(r.json()['status']))
        db.session.commit()

        responses["Message"] = SMS_SERVICES['SUCCESS']
        responses['status'] = r.json()['status']
        responses['status_code'] = r.status_code
        return responses

    #end def


    def postSingleCustom(self, payload) :
        ''' tell to api to send post information '''
        responses = {} #"text"              : payload['text'],

        # build payload
        data = {
            "destination"       : payload['destination'],
            "country"           : payload['country'],
            "encoding"          : API_SERVICES.ENCODING,
            'text'              : API_SERVICES.TEXT,
            "source"            : payload['source']
            }

        if 'text' in payload:
            data['text'] = payload['text']
        #end if


        result = self.postSingleCustomtoAPI(data)
        if result['status_code'] != 200 :
            responses["status"] = "FAILED"
            responses["data"  ] = SMS_OTP_ERRORS["FAILURE"]
            responses['status_code'] = result['status_code']
            responses['message'] = result['message']
            return responses
        if result == "REQUEST_TIMEOUT":
            responses["status"] = "FAILED"
            responses['status_code'] = result['status_code']
            responses["data"  ] = SMS_OTP_ERRORS["TIMEOUT"]
            return responses
        if result == "BAD_URL":
            responses["status"] = "FAILED"
            responses['status_code'] = result['status_code']
            responses["data"  ] = SMS_OTP_ERRORS["REDIRECT"]
            return response
        if result == "EXCEPTION":
            responses["status"] = "FAILED"
            responses['status_code'] = result['status_code']
            responses["data"  ] = SMS_OTP_ERRORS["EXCEPTION"]
            return responses
        #end if
        return result
    #end def

    def postBatchtoAPI(self, data) :
        ''' post information to API wavecell for single message but in many number destination'''
        API_NAME = "batch_sms"
        responses = {}

        headers = {
            "content-type": "application/json"
        }
        headers["Authorization"] = "Bearer {}".format(API_SERVICES.API_KEY)
        log = BatchSms(amount_destination=len(data['messages']),
                        provider=SMS_SERVICES['PROVIDER'],
                        api_name=API_NAME,
                        sms_request=data)
        start_time = time.time()
        db.session.add(log)


        try:
            r = requests.post(
                SMS_SERVICES['SMS_API']["BATCH_API"],
                data=json.dumps(data),
                headers=headers,
            )
            if r.status_code != 200:
                for status in r.json()['messages']:
                    log.set_status_request(dict(status['status']))
                log.save_response_time(time.time() - start_time)
                responses['status_code'] = r.status_code
                responses['message'] = r.json()['message']
                return responses
            #end if
        except requests.exceptions.Timeout:
            return "REQUEST_TIMEOUT"
        except requests.exceptions.TooManyRedirects:
            return "BAD_URL"
        except requests.exceptions.RequestException as e:
            print(str(e))
            return "FAILURE"
        #end try

        log.save_response_time(time.time() - start_time)
        log.save_response(dict(r.json()))
        log.set_accepted_account(int(r.json()['acceptedCount']))
        log.set_rejected_account(int(r.json()['rejectedCount']))
        for status in r.json()['messages']:
            log.set_status_request(dict(status['status']))
        db.session.commit()

        responses["message"] = SMS_SERVICES['SUCCESS']
        responses['accepted'] = r.json()['acceptedCount']
        responses['rejected'] = r.json()['rejectedCount']
        responses['status_code'] = r.status_code

        return responses
    #end def


    def postBatch(self, payload) :
        ''' tell to api to send post information '''
        responses = {}

        # build payload
        for clientId in range(len(payload)) :
            payload['clientBatchId'] = "Modana_000" + str(clientId)


        for destination in payload['messages'] :
            destination['text']         = API_SERVICES.TEXT
            destination['encoding']     = API_SERVICES.ENCODING
        
        data = payload

        result = self.postBatchtoAPI(data)
        if result['status_code'] != 200 :
            responses["status"] = "FAILED"
            responses["data"  ] = SMS_OTP_ERRORS["FAILURE"]
            responses['status_code'] = result['status_code']
            responses['message'] = result['message']
            return responses
        if result == "REQUEST_TIMEOUT":
            responses["status"] = "FAILED"
            responses['status_code'] = result['status_code']
            responses["data"  ] = SMS_OTP_ERRORS["TIMEOUT"]
            return responses
        if result == "BAD_URL":
            responses["status"] = "FAILED"
            responses['status_code'] = result['status_code']
            responses["data"  ] = SMS_OTP_ERRORS["REDIRECT"]
            return responses
        if result == "EXCEPTION":
            responses["status"] = "FAILED"
            responses['status_code'] = result['status_code']
            responses["data"  ] = SMS_OTP_ERRORS["EXCEPTION"]
            return responses
        #end if
        return result
    #end def

    def postBatchCustomtoAPI(self, data) :
        ''' post information to API wavecell for single message but in many destination number and text custom form'''
        
        API_NAME = "batch_sms_custom"
        responses = {}

        headers = {
            "content-type": "application/json"
        }
        headers["Authorization"] = "Bearer {}".format(API_SERVICES.API_KEY)

        log = BatchSms(amount_destination=len(data['messages']),
                        provider=SMS_SERVICES['PROVIDER'],
                        api_name=API_NAME,
                        sms_request=data)
        start_time = time.time()
        db.session.add(log)

        try:
            r = requests.post(
                SMS_SERVICES['SMS_API']["BATCH_CUSTOM_API"],
                data=json.dumps(data),
                headers=headers,
            )
            if r.status_code != 200:
                for status in r.json()['messages']:
                    log.set_status_request(dict(status['status']))
                log.save_response_time(time.time() - start_time)
                responses['status_code'] = r.status_code
                responses['message'] = r.json()['message']
                return responses
        except requests.exceptions.Timeout:
            return "REQUEST_TIMEOUT"
        except requests.exceptions.TooManyRedirects:
            return "BAD_URL"
        except requests.exceptions.RequestException as e:
            print(str(e))
            return "FAILURE"
        #end try

        log.save_response_time(time.time() - start_time)
        log.save_response(dict(r.json()))
        log.set_accepted_account(int(r.json()['acceptedCount']))
        log.set_rejected_account(int(r.json()['rejectedCount']))
        for status in r.json()['messages']:
            log.set_status_request(dict(status['status']))
        db.session.commit()

        responses['message'] = SMS_SERVICES['SUCCESS']
        responses['accepted'] = r.json()['acceptedCount']
        responses['rejected'] = r.json()['rejectedCount']
        responses['status_code'] = r.status_code
        return responses
    #end def


    def postBatchCustom(self, payload) :
        ''' tell to api to send post information '''
        responses = {}

        # build payload
        # text in payload need to be filled in front 
        for destination in payload['messages'] :
            destination['encoding']     = API_SERVICES.ENCODING
        #end for

        for message in payload['messages']:
            if 'text' not in message:
                message['text'] = API_SERVICES.TEXT
            #end if
        #end for

        payload['includeMessagesInResponse'] = True

        data = payload

        result = self.postBatchCustomtoAPI(payload)
        if result['status_code'] != 200 :
            responses["status"] = "FAILED"
            responses["data"  ] = SMS_OTP_ERRORS["FAILURE"]
            responses['status_code'] = result['status_code']
            responses['message'] = result['message']
            return responses
        if result == "REQUEST_TIMEOUT":
            responses["status"] = "FAILED"
            responses['status_code'] = result['status_code']
            responses["data"  ] = SMS_OTP_ERRORS["TIMEOUT"]
            return responses
        if result == "BAD_URL":
            responses["status"] = "FAILED"
            responses['status_code'] = result['status_code']
            responses["data"  ] = SMS_OTP_ERRORS["REDIRECT"]
            return responses
        if result == "EXCEPTION":
            responses["status"] = "FAILED"
            responses['status_code'] = result['status_code']
            responses["data"  ] = SMS_OTP_ERRORS["EXCEPTION"]
            return responses
        #end if
        return result
    #end def
#end class


