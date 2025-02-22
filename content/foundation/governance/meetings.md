Title:     Apache Corporate Governance - New Member Voting
license: https://www.apache.org/licenses/LICENSE-2.0

The ASF holds an Annual Members Meeting at least every 13 months, where a new board of directors is elected, and new member candidates may be voted upon.  
Our corporate meetings are run by our Member volunteers following these basic procedures.

[TOC]

# Audience  {#audience}

This document is a general overview of how the ASF holds it's formal Member's Meetings.  If you are a Member of the ASF, please see the private README.txt of the current year's meeting for the latest details in:
    `/repos/private/foundation/Meetings/20200331/README.txt`

# Meeting Mechanics - On IRC Chat  {#meetinghow}

Since our Membership is from around the globe, Member Meetings are held on freenode's IRC chat during a period of three days.  The first half of the meeting (typically Tuesday) in held in a live IRC chat where all Members are invited to attend.  Much like any large meeting, we hold a roll call, and the Chair of the Board runs us through the posted agenda interactively in the live chat window.  During the first half of the meeting, we review high-level reports from various executive officers reporting on the state of the Foundation in the past year.  Members who aren't able to attend during this first half may submit a proxy, so that their attendance can still be marked to count for quorum.

At the end of the first half of the meeting, the agenda lists the candidates for the next year's board, as well as any new candidates for membership in the Foundation.  Once the candidates are announced, the meeting is moved into a ~46 hour recess.

During the recess, our [Apache STeVe voting software](https://steve.apache.org/) sends out secure and private email ballots to all eligible members.  Voting is open for over 40 hours via email, allowing Members anywhere in the world a convenient time to cast their ballots.  All election counting and tracking is performed by Apache STeVe and several Member volunteer election monitors.  Votes are cast using a simple web interface after logging in with your Apache ID.

Voting closes a couple of hours before the meeting resumes (typically on Thursday) to give election monitors to cross-check that each of their tallies agrees.  When the meeting resumes on IRC, the Chair announces the results of member candidate and board elections are announced in the meeting. The second half of the meeting is typically much shorter, and Members do not need to attend the second half if they have already attended the first half.

- **PLEASE** don't wait until the last minute to cast your vote: our vote monitors are all volunteers.  Since all of the candidates for board and new members are listed 10 days before the meeting, you have plenty of time beforehand to research your choices.


Immediately after the meeting, the new board is installed and announced for their year term, and private invitations are sent out to the lucky new member candidates by existing Members who nominated them.  Note that we do **not** publicize the names of newly elected members, because (rarely) some do not complete the new member application.

# Member Candidate Voting  {#membervoting}

## How Member Votes Are Tallied ##

For a new member to be elected, he/she must receive more Yes votes than No votes from the Members who cast a vote in their nomination, [per our bylaws 4.1][1].   All vote tracking and tallies are handled by the Apache STeVe code, as monitored by our volunteer vote monitors.  The process of running and auditing votes are all done by ASF Members privately.

Votes for new member candidates are secret; since the votes are about individual people, once the vote monitors have confirmed the tallies result in an election (or not), they are not shared.

## How To Decide How To Vote On Member Candidates ##

That's completely up to every ASF Member to decide.  New member candidates are nominated by an existing member, who posts a description of why they believe the candidate would make a good member.  There are very often seconds of the nomination, many of which also include personal stories of why the candidate should be elected.

Since new candidates are people who are involved in Apache projects, many people search the many mailing lists to see how the candidate has participated in our communities in the past.  Using [PonyMail's archives](https://lists.apache.org/) is easy - where ASF Members can review all mailing lists, even private ones.

Many members have commented that they look for both a strong nomination statement from an existing member, describing why the nominee would make a good candidate. Having a number of seconds in the nomination file of other members is also often valuable.

# Boad of Directors Voting  {#boardvoting}

## How Votes For The Board Are Tallied ##

The ASF uses Single Transferable Votes (STV) to elect all 9 seats on the board annually.  Every candidate runs individually; there is no slate or block of candidates.  Only ASF Members can nominate people for the board election; and in the past all candidates have already been ASF Members.

STV is designed to help small coherent constituencies elect a director to the board. This vote counting design helps to enable voters to reveal their actual desires and avoid being too clever. Read on for a discussion of how we use STV, including details of how our volunteer vote monitors actually tally up the votes.

The most important thing to remember is: Vote the actual order of your preferences! Every effort is made to get your #1 preference onto the board; #1 votes are notably more important than the rest of your votes. If you vote in alphabetical order (as some seem to have done with past ballots) you're sending a strong signal that you'd prefer a board with names like Mr. Awful and Ms. Beastly - probably not what you intended. Our Apache STeVe tool randomizes the letters assigned to candidates to attempt to help with this.

Election results are calculated using Meek's Method for STV.  Technical details are in the [Apache STeVe project code](https://svn.apache.org/viewvc/steve/trunk/), which is of course it's own Apache project.

STV vote counting proceeds in a loop. The loop spits out a name whenever a board candidate captures enough ballots to get elected. Ballots begin by being assigned to the #1 candidate indicated on that ballot. As the counting proceeds ballots are reallocated. Sometimes it becomes necessary to admit somebody is not going to get elected; at that point, their ballots are reallocated. When a candidate is elected he or she takes with them only enough ballots to have gotten him elected; their other ballots are sent off the lower ranked preferences shown on that ballot.

This YouTube video provides a delightful introduction: [Politics in the Animal Kingdom: Single Transferable Vote](https://www.youtube.com/watch?v=l8XOZJkozfI) or a shorter [description of how second, third, etc. place votes are allocated](https://youtu.be/Ac9070OIMUg).  Wikipedia has a general overview of [Single Transferable Voting](http://en.wikipedia.org/wiki/Single_Transferable_Vote).

## How To Decide How To Vote On Board Candidates ##

Obviously, this is up to every ASF Member to decide.  The fact that all Members - and all candidates for the board - are expected to act as individuals means that our corporate governance is never beholden to other corporations or people's employers.  This independence of the board is a key factor in the ASF's success over the years.

- STV votes are ranked; the first person you vote for is far more likely to get your vote than the second (and so on).
- If you really don't want somebody on the Board, then omit them entirely, rather than putting them at the end.
- Although there are 9 slots available, you can vote for as many people as you want - even votes after the 9th might possibly end up being significant. Note that people you don't want to be elected should not appear on your list at all.
- By example, if 89 members vote in the election, a candidate can win one of the nine seats on the board with just 10 #1 votes. This helps to assure small constituencies with first place preferences can get a board seat.
- AND RECALL: The ORDER of your votes is CRUCIAL!  Double-check your ballot before submitting
- You can cast your vote for the board as many times as you like; only the **last ballot cast** will be used.  So if you make a mistake, or change your mind, just cast that vote again.


  [1]: https://www.apache.org/foundation/bylaws.html#4.1
