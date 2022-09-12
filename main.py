from flask import Flask

app = Flask(__name__)

@app.route('/')

def ddt():
   return f"""<h3>Юрий Шевчук</h3> <br>
   <img src= {"https://i.ytimg.com/vi/d28c2yzwVEs/hqdefault.jpg"}> <br>
   
   <strong><p><mark>Юрий Юлианович Шевчук</mark> - российский рок-музыкант, автор песен, продюсер, 
   актёр и художник. <br> Основал и до сих пор остаётся единственным бессменным 
   участником, лидером коллектива «ДДТ».  <br> Его творчество имеет гражданственно-патриотическое 
   и социально-сатирическое направление. <br> В 2003 году удостоен звания Народного артиста Республики 
   Башкортостан.<br> Ю.Ю.Шевчук живет в Санкт-Петербурге
   и является настоящим гражданином и патриотом России. </p> <br>
   Это последний клип группы ДДТ <mark>"Не с вами"</mark> </strong>  <br>
   <iframe width="560" height="315" src="https://www.youtube.com/embed/Jbyx3TfjotY" title="YouTube video player" 
   frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
   allowfullscreen></iframe> <br>
   <p><em><a href= "https://ddt.ru/">А вот здесь, мои касатики, ссылка на страницу группы ДДТ</a></em></p>
   <mark>Миру-Мир</mark>
   """

app.run()
