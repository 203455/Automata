exports.handler = (event, context) =>{
    var req = event.request
    var res = makeResponse("Funcion")

    try {
        if (req.type === 'LaunchRequest') {
            res = makeResponse('Si te sientes mal, estoy segura que te puedo decir algo para ayudarte')
        } else{
            if (req.type === 'IntentRequest') {
                switch (req.intent.name) {
                    case 'HelloIntent':
                        res = makeResponse('A veces las cosas no son como deberían ser, lo importante es permanecer')
                        break;
                    case 'DisplayGreetings':
                        res = handleDisplayGreetings(req.intent)
                        break
                    case 'FavoriteLanguage':
                        res = handleFavoriteLanguage(event)
                    default:
                        break;
                }
            }
        }
    } catch (error) {
        context.file(error)
    }

    function handleDisplayGreetings(intent) {
        var name = intent.slots.PersonName.value;
        return makeResponse(`Bienvenido de vuelta ${name}. Espero puedas tener hoy una gran día `, {
            'PersonName': name
        } )
    }

    function handleFavoriteLanguage(event) {
        return makeResponse('Cuando te sientas solo, recuerda que solo es un reencuentro contigo mismo.')
    }

    function makeResponse(text, sessionData) {
        var res = {
            "version" : "1",
            "response": {
                "outputSpeech":{
                    "type": "PlainText",
                    "text": text
                },
                "shouldEndSession": false
            }
        };

        if (sessionData) {
            res.sessionAtributes = sessionData
        }

        return res;
    }
}