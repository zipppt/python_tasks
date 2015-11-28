# -*- coding: cp866 -*-


Feature: RADT-I
  Scenario: Simple pass RADT-I
    Given website "http://ccapp-test.marpasoft.com/"
    When enter login "zipppt@gmail.com" and password "zipppt2016"
    Then is logged in as "zipppt"
    When enter CADC-I
    Then is CADC-I in as "Certified Alcohol Drug Counselor I (CADC-I)"
    When enter PersonaInformation form CADC-I
    When Submit
    When Traditional Method
    When Apply1
    When Form2
    When Apply2
    Then Clean