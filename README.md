discord-bot-elvan-kodland (Language of bot Indonesia)
experimental discord bot backed by python 3 and discord API
	
	# function initialization by $ prefix
 	# e.g. $pw
	bot = commands.Bot(command_prefix='$', intents=intents, help_command= None)
	@bot.event # decorator to modify python function itself for anything happens with server
	@bot.command() # calls the function to run

	functions that is used:

	async def on_ready() := to indicate that the bot have logged in
	async def on_message(msg) := to respond of greeting Hello, Hi, or Test
	async def on_member_join(member) := greeting new member to server and how to start
	async def hello(ctx) := function to send what the bot can do
	async def help(ctx) := contact detail of the developer
	async def coinflip(ctx) := to flip head or tail of the coin
	async def dice(ctx) := to roll dice from 1 to 6
	async def pw(ctx) := to generate a random password with 10 digits
	def get_dog_image_url() := to work with API to get the image from url
	async def dog(ctx) := send the image dog to general chat
	def get_duck_image_url() := to work with API to get the image from url
	async def duck(ctx) := send the image dog to general chat
	async def dt(ctx, arg) := to get the meaning of modern wording or emoji
	async def load(ctx) := to load the new Cogs file(class)
	async def unload(ctx) := to unload the Cogs
	async def reload(ctx) := to reload the Cogs file(class) so the bot will keep runing even there is new update or feature
	async def setalarm(self,ctx,date) := to set alarm   	
