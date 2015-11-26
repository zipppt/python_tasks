# -*- coding: cp866 -*-


Feature: RADT-I
  Scenario: Simple pass RADT-I
    Given website "http://ccapp-test.marpasoft.com/"
    When enter login "zipppt@gmail.com" and password "zipppt2016"
    Then is logged in as "zipppt"
    When enter RADT-I
    Then enter PersonaInformation form Radt1
    Then doSubmit
    Then doRegHis
    Then doApply
    Then doClean


