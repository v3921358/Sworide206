from https://forum.ragezone.com/f427/java-v206-source-swordie-base-1206889/

#A server emulator for Maplestory.


Greetings,

This release is happening because I want to leave something behind while I step away to get myself in a better mental place. Hopefully this release will help others contribute back to the community and help move the open-dev community to a higher revision.

This is a v206 based source which has been sold around the internet / Discord. Credits go to each respective individual for their hard work, I will leave them out for privacy (unless they want credit). Use IntelliJ to run, MySQL for database.

[Features]
All Classes work
Some Bosses work (Not 100% which ones work and which don't, some were fixed, others not)
Cash Shop Works (Has most, if not entire WZ Directory added into the SQL database)
Guilds Work
Custom Quick Move
Others, check in game / source code to see

[Quick Tutorial]
*Check Pom.xml to see what requirements are needed (Open JDK 17, MySQL 5.1.39)
1) Open the folder in IntelliJ and wait for everything to index.
2) Go to src/main/java/ and open hibernate.cfg.xml. Add your MySQL Password under Password, change username root if you have a different username for MySQL.
3) Check File Structure (CTRL+ALT+SHIFT+S) to ensure you have OpenJDK 17 selected.
4) Open MySQL and create a new database v206, run each individual .sql file inside the main folder / sql from 1-10 in order, plus the extras at the bottom.
5) go to src/main/java/net.swordie.ms/ and right-click Server and click Run or Debug. If everything is setup properly, the last item loaded into Console will be channels.

Download: https://1fichier.com/?z390t7e8lxggwb8uyz2j

Auth Hook & Launhcer + v206 Client: https://forum.ragezone.com/f921/rele...0/#post9135498

Thanks to those who were there for me, and thanks to everyone for the fun times.