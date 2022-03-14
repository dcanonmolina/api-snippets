<?php
require_once './vendor/autoload.php';
use Twilio\TwiML\VoiceResponse;

$response = new VoiceResponse();
$pay = $response->pay(['chargeAmount' => '10.00', 'paymentConnector' => 'My_Generic_Pay_Connector', 'action' => 'https://your-callback-function-url.com/pay']);
$pay->parameter(['name' => 'custom_parameter_1', 'value' => 'custom_value_1']);

echo $response;