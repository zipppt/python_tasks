# -*- coding: cp866 -*-


Feature: RADT-I
  Scenario: Simple pass RADT-I
    Given website "http://ccapp-test.marpasoft.com/"
    When enter login "zipppt@gmail.com" and password "zipppt2016"
    Then is logged on

    Then enter PersonaInformation form Radt1
    Then doSubmit
    Then doRegHis
    Then doApply

    Then doClean


