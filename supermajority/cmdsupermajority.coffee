# Supermajority Calculator
# @description: This script calculates the supermajority of a vote based
# on the number of voters and the number of votes for each category.
# @author: @StrawberryMaster
# @note: created using CoffeeScript

voteResults = [
  {vote: "Support", value: 100},
  {vote: "Neutral Leaning Support", value: 75},
  {vote: "Neutral", value: 50},
  {vote: "Neutral Leaning Oppose", value: 25},
  {vote: "Oppose", value: 0}
]

totalVoters = 0
totalValue = 0

for result in voteResults
  result.count = parseInt(prompt("Enter the number of votes for the '#{result.vote}' category:"))
  totalVoters += result.count
  totalValue += result.value * result.count

supermajority = totalValue / totalVoters

formattedSupermajority = supermajority.toString().slice(0, 5)

console.log "The supermajority is #{formattedSupermajority}%"

if supermajority >= 60
  console.log "The vote passes!"
else
  console.log "The vote fails."
