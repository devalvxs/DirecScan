
from colorama import init, Fore, Back

init()

import requests

diretorios=["admin","config","logs","uploads","scripts","backup","backups","temp","auth","senhas","wp-admin","wp-content","database","images","public","private","security","sql","users","root","assets","sessions","api","download","documents","mail","videos","settings","cache","tools","archives","test","dev","sys","web","html","info","cgi-bin","tmp","stats","error","system","login","signup","shopping","billing","support","contact","feedback","subscribe","unsubscribe","terms","privacy","faq","about","news","press","jobs","career","opportunities","partners","clients","vendors","services","products","portfolio","pricing","payment","cart","checkout","order","forum","community","blog","articles","events","calendar","resources","help","index","home","default","page","landing","welcome","error404","error500",".git",".svn",".DS_Store",".htaccess",".env","phpmyadmin","webadmin","webmaster","admin_panel","admin_area","admin_login","admin_page","admin_section","admin_tool","administrator","adminportal","adm","control_panel","user","usr","usr/local","usr/bin","usr/sbin","usr/share","usr/lib","usr/include","usr/src","usr/man","usr/games",".well-known","demo","examples","uploads_tmp","uploads_temp","upload_tmp","upload_temp","uploader","configuration","setting","manage","manager","manage_page","manage_pages","manage_panel","manage_section","manage_sections","sitemap.xml","crossdomain.xml","apple-touch-icon.png","apple-touch-icon-precomposed.png","apple-touch-icon-120x120.png","apple-touch-icon-120x120-precomposed.png","apple-touch-icon-152x152.png","apple-touch-icon-152x152-precomposed.png","apple-touch-icon-180x180.png","apple-touch-icon-180x180-precomposed.png","apple-touch-icon-192x192.png","apple-touch-icon-192x192-precomposed.png","apple-touch-icon-256x256.png","apple-touch-icon-256x256-precomposed.png","apple-touch-icon-512x512.png","apple-touch-icon-512x512-precomposed.png","apple-touch-icon-1024x1024.png","apple-touch-icon-1024x1024-precomposed.png","robots.txt.bak","robots.txt~","robots.bak",".htpasswd",".htgroup",".htaccess.old",".htaccess.txt",".htaccess.bak",".htpasswd~",".htgroup~",".htpasswd.old",".htgroup.old",".htusers","error_log","access_log","error.log","access.log","error.txt","access.txt","errorlog","accesslog","errorlog.txt","accesslog.txt","errorlog.bak","accesslog.bak","errorlog~","accesslog~","error_log~","access_log~","shadow","hidden","cloak","invisible","mystery","stealth","underground","masked","sneak","covert","darkness","unknown","concealed","furtive","clandestine","cryptic","unseen","subterranean","shadowy","secretive","mystic","confidential","enigma","veiled","mysterious","incognito","cloak-and-dagger","obscure","camouflaged","stealthy","esoteric","privileged","restricted","undercover","forgotten","neglected","ignored","overlooked","abandoned","secluded","remote","isolated","discreet","unnoticed","undetected","unrevealed","unspoken","unacknowledged","unobserved","unrecognized","unsolved","unresolved","unexplained","mystique","intrigue","secrecy","obscurity","hiddenness","privateness","obfuscation","covertness","obscurantism","hush-hush","off-the-record","behind-the-scenes","classified","top-secret","eyes-only","need-to-know","behind-closed-doors","under-the-table","off-limits","inaccessible","off-the-grid","off-the-radar","off-the-map","off-the-beaten-path","under-the-radar","under-wraps","under-the-counter","behind-locked-doors","behind-the-veil","restricted-access","privileged","forbidden","sealed","untouchable","undivulged","uploads_tmp","upload","uploads","uploads_temp","upload_tmp","upload_temp","uploader","temporary","temp","tmp","script","control","controls","console","sitemap.xml","crossdomain.xml","favicon.ico","robots.txt","sitemap.xml","crossdomain.xml","favicon.ico","robots.txt.bak","robots.bak",".htpasswd.old",".htgroup.old",".htusers","error.log","access.log","error.txt","access.txt","errorlog","accesslog","errorlog.txt","accesslog.txt","errorlog.bak","accesslog.bak","errorlog~","accesslog~","error_log~","access_log~","db","sql","mysql","sql_dump","sql_backup","database_backup","db_backup","dump","database_dump","db_dump","mysql_dump","mysql_backup","backup_db","backup_sql","backup_mysql","sql_database","mysql_database","database_sql",".git",".svn","phpmyadmin","wp-content/plugins","wp-includes"]

from colorama import init, Fore, Back

init()    


print(Fore.LIGHTMAGENTA_EX+"Varios links podem ser escaneados mais de uma vez para confirmação!")

site=input(Fore.LIGHTYELLOW_EX+"URL do site que deseja escanear: ")           

if not site.endswith(".com"):
    site += ".com"

for pasta in diretorios:
 
    if site.endswith("/"):          
        teste = site + pasta
    else:                                     
        teste = site + "/" + pasta

    if not site.startswith("https://"):            
        teste = "https://" + site + "/" + pasta

    if site.endswith("/") and not site.startswith("https://"):      
        teste = "https://" + site + pasta
    

    requisicao = requests.get(teste)    
    
    
    if requisicao.status_code >= 200 and requisicao.status_code < 300:             
        print(Fore.GREEN + "Diretório encontrado! - |" + teste)                                    
    elif requisicao.status_code >= 400 and requisicao.status_code < 500:
        print(Fore.RED + "Não encontrado ou Negado! - |" + teste)
    elif requisicao.status_code >= 500 and requisicao.status_code < 600:         
        print(Fore.YELLOW + "Erros de Servidor! - |" + teste)
    elif requisicao.status_code >= 300 and requisicao.status_code < 400:
        print(Fore.CYAN + "Redicionado! - |" + teste)
    elif requisicao.status_code >= 100 and requisicao.status_code < 200:
        print(Fore.LIGHTMAGENTA_EX + "Resposta de informação! - |"  + teste)