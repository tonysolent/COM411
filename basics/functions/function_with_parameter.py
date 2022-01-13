def escape_by(plan) :
    plan1 = "jumping over"
    plan2 = "running around"
    plan3 = "going deeper"
    if plan == plan1 :
        print("We cannot escape that way! The boulder is too big!\n")
    if plan == plan2 :
        print("We cannot escape that way! The boulder is moving too fast!\n")
    if plan == plan3 :
        print("That might just work! Let's go deeper!\n")
escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")