import turtle as t
def d():
 k,s=__import__("random").random()*100,1.414
 def x(a=1,b=90):
  t.fd(k*a);t.lt(b);return x
 x()(1.5)(.25)(.5)(.25,180)()(b=135)(s)(s/2)(s/2)(s,45)
exec("d();"*5)
t.exitonclick()
