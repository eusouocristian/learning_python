import messagebird
client = messagebird.Client('l6AqewjeVnuy1NcfGET76lLIk')
message = client.message_create('MessageBird',
                                '+5551998034545',
                                'Eu te amo muitão. (mandando via Python)',
                                {'reference': 'Foobar'})
