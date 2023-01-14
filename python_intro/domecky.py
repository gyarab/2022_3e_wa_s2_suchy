import turtle as t
def d():
 k,n,s=__import__("random").random()*100,135,1.414
 def x(a=1,b=90):
  t.forward(k*a);t.left(b);return x
 x()(1.5)(.25)(.5)(.25,n)(s/2)(s/2,45)(1,n)(s,n)(1,n)(s,45)
exec("d();"*5)
t.exitonclick()
