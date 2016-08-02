Feature: Scenario Outline
  Scenario Outline: Blenders
     Given I put "<thing>" in a blender
     When I switch the blender on
     Then it should transform into "<other thing>"
   Examples: Amphibians
     | thing         | other thing |
     | Red Tree Frog | mush        |
     | apples        | apple juice |
   Examples: Consumer Electronics
     | thing         | other thing |
     | iPhone        | toxic waste |
     | Galaxy Nexus  | toxic waste |