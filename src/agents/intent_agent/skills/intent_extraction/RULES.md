# Extraction Rules

## Rule 1

Each intent must represent one atomic user action.

## Rule 2

Preserve all contextual information associated with the action.

Examples:

- location information
- page references
- popup references
- header references
- relative positioning

## Rule 3

Do not remove descriptive details.

Examples:

- first relevant search result
- second search button
- popup containing text Individual Investors

## Rule 4

Do not generate locators.

Allowed:

- search box in header
- popup containing Individual Investors

Not Allowed:

- xpath
- css selector
- id
- name attribute

## Rule 5

Do not generate automation code.

## Rule 6

Intents must be returned in execution order.

## Rule 7

Step numbering must begin at 1 and remain sequential.

## Rule 8

Do not merge multiple actions into one intent.

## Rule 9

Do not infer actions not present in the requirement.

## Rule 10

Preserve conditional instructions when present.