# -*- coding: cp866 -*-


#Укажем что это за фича
Feature: Checking search
#Укажем имя сценария (в одной фиче может быть несколько)
Scenario: Сheck some text in search results
#И используем наши шаги.
  Given website "http://ccapp-test.marpasoft.com/"
  Then enter login and the password
  Then enter PersonaInformation form Radt1
  Then doSubmit
  Then doRegHis
  Then doApply
  Then doClean


