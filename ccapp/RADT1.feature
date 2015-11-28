# -*- coding: cp866 -*-


Feature: RADT-I
  Scenario: Simple pass RADT-I
    Given website "http://ccapp-test.marpasoft.com/"
    When enter login "zipppt@gmail.com" and password "zipppt2016"
    Then is logged in as "zipppt"
    When enter RADT-I
    Then is RADT-I in as "Requirements for applying for Registered Alcohol and Drug Trainee I:"
    When enter PersonaInformation form Radt1
    When Submit
    When RegHis
    When Apply
    Then Clean