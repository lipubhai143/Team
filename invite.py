from team import FF_CLIENT, map_team_number
import logging

def handler(request, response):
    try:
        uid = request.args.get("uid")
        team_input = request.args.get("team", "4")

        if not uid or not uid.isdigit():
            return response.status(400).json({ "error": "Invalid or missing UID" })

        if not team_input.isdigit() or int(team_input) not in [3,4,5,6]:
            return response.status(400).json({ "error": "Team must be 3, 4, 5, or 6" })

        team_number = map_team_number(int(team_input))

        logging.info(f"Inviting UID {uid} to team {team_number}")

        bot = FF_CLIENT(
            id="4046916457",
            password="53A01F233F08B3BABCFE74F1C563BE4D2D2BB8FF7A28178C04A99A2CCE519C47",
            target_uid=int(uid),
            team_number=team_number
        )
        bot.start()
        bot.join()

        return response.status(200).json({
            "success": True,
            "message": f"UID {uid} invited to team {team_input}"
        })

    except Exception as e:
        return response.status(500).json({ "error": str(e) })
