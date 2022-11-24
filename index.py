import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world!!")

class staticRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class queryRequestHandler(tornado.web.RequestHandler):
    def get(self):
        n = int(self.get_argument("n"))
        r="odd" if n % 2 else "even"

        self.write(f"The number {n} is {r}")

class resourceRequestHandler(tornado.web.RequestHandler):
    def get(self,id):

        self.write(f"Querying tweet {id}")
            



if __name__ == "__main__":
    app = tornado.web.Application([(r"/",basicRequestHandler),
    (r"/static",staticRequestHandler),
    (r"/isEven",queryRequestHandler),
    (r"/tweet/([0-9]+)",resourceRequestHandler)])

    app.listen(8881)

    print("I.m listening on port 8881")
    tornado.ioloop.IOLoop.current().start()