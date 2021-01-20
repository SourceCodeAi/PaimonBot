from dhooks import Webhook
import discord
import csettings

hook = Webhook("https://discord.com/api/webhooks/793839123957940254/RmhYZRQADYYYw--IPBK29lj891yETDcJVNkLAke1sXO4VoYi_c87IiKedAFS0R5xhjc0")

embed = discord.Embed(
    colour = csettings.embedcolour(),
    title = "Staff Info",
    description = "[] = Required Arguments | <> = Good To Have But Not Required Arguments",
)
embed.add_field(name = "Moderator Commands", value = "To mute a member, run the `?mute [member] [duration] <reason>` command! This will mute the member via Carl Bot! To warn a member, run the `?warn [member] [reason]` command! This will warn the member via Carl Bot!", inline = False)
embed.add_field(name = "Administrator Commands", value = "To ban a member, run the `pmn ban [member] <reason>` command! This will ban the member via Paimon Bot! To kick a member, run the `pmn kick [member] <reason>` command! This will kill the member via Paimon Bot!", inline = False)
embed.add_field(name = "Utils", value = "Administrators can run Moderator Commands!", inline = False)



hook.send(embed = embed)

