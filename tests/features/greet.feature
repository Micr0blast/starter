Feature: Agent greets user
    Scenario: Agent greets users cheerfully
        Given there is an agent
        And there is a user
        And user has given a name
        When user provides the name
        Then agent greets user cheerfully by name 
        