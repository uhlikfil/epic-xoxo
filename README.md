# epic-xoxo

## Implementované servisy

### Web UI +Nginx
Webové rozhraní pro klienty je napsané ve framewroku Vue.js, které následně distribuuje Nginx.

### Netflix Zuul
Netflix Zuul se používá jako inverse proxy a load balancer.

### Game Service
Zprostředkovává online hraní. Umožňuje trackování místností vytvořenými různými hráči a synchronizuje stav hry mezi nimi.

Protože game service je postavená na technologii WebSocket, kterou Netflix Zuul nepodporuje, klienti se napojí na Game Service napřímo.

### Eureka
Do Eureky se reigstrují služby pro service discovery.

### RabbitMq
Message broker.

### Replay Service
Sdružuje všechny dohrané hry online a vystavuje jejich záznamy, umožňuje záznamy filtrovat a vyhledávat.

### Users Service
Log-in-less user management, který sleduje, na jaké IP adrese odehrál uživatel poslední hru.

Funguje také jako agregace dat z dalších servis (momentálně pouze Highscore) pomocí endpoinu userdetail.

### Highscore Service
Ukládá počet vyhraných/prohraných/opuštěných her pro jednotlivé uživatele a zprostředkovává žebříček nejlepších hráčů podle poměru vyhraných her.
