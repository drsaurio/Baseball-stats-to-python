# Project 3: Data Analtics
# Created by: Pedro C.Palomino



#SLG = H+2B+(2*3B)+(3*HR)/AB
#AB:Bats/ 2B:Dobles/3B triples/H:Hits/HR:Hruns

print("\nBaseball Players Stats in Major League Baseball in 2013. What would you like to do?")


choice = ''


while choice != 'QUIT':
  
    print("\n[1] Enter 2013 to see an example.")
    print("[2] Enter TEAM to choose your team information.")
    print("[3] Enter REPORT to see the stats.")
    print("[4] Enter HELP for more information about the teams .")
    print("[5] Enter QUIT to quit.")
    
    
    choice = input("\nWhat would you like to do? ")
    
# JUST AN EXAMPLE

    if choice == '2013':
        print("\nGeneral Stats" + "\n")
        team = open('scores.txt', 'r')
        print ("_"*95) 
        print ("| Last names | Fist names | Teams | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns | ")
        print ("_"*95)       
        for player in team:
            values = player.split()
            print("|",'{0:10}'.format(values[0]),"|",
                  '{0:10}'.format(values[1]),"|",
                  '{0:5}'.format (values[2]),"|",
                  '{0:7}'.format (values[3]),"|",
                  '{0:4}'.format (values[4]),"|",
                  '{0:6}'.format (values[5]),"|",
                  '{0:4}'.format (values[6]),"|",
                  '{0:7}'.format (values[7]),"|",
                  '{0:6}'.format (values[8]),"|",
                  '{0:5}'.format (values[9]),"|")
        print ("-"*95) 
        print("\n")     

#TEAM: THE PROGRAM WILL DISPLAY ALL INFORMATION ABOUT ALL PLAYERS ON THAT TEAM.
          
    elif choice == 'TEAM':
        print("\n")
        print("2013 stats by Baseball Teams" + "\n")
       
        teams = input("Insert the name of your team to get the stats: ")
        print("\n")
        
        if teams =='BAL':
         print ("_"*87)    
         print ("| Last names | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns | ")
         print ("_"*87) 
         lista = [];
         def buscaPalabra(str, file):       
            for line in file:
                line = line.replace("\n", "")
                line = line.replace(";", "")
                line = line.replace(",", "")
                for part in line.split():
                   if str in part:
                       lista.append(line);
                       line = line.split()
                       print( "|",'{0:10}'.format(line[0]),"|",
                       '{0:10}'.format(line[1]),"|",
                       '{0:7}'.format (line[3]),"|",
                       '{0:4}'.format (line[4]),"|",
                       '{0:6}'.format (line[5]),"|",
                       '{0:4}'.format (line[6]),"|",
                       '{0:7}'.format (line[7]),"|",
                       '{0:6}'.format (line[8]),"|",
                       '{0:5}'.format (line[9]),"|")       
            return lista
         file = open('2013.txt','r')
         (buscaPalabra("BAL", file))
         print ("-"*87) 
         print("\n")  
       
         
        elif teams == 'CHC':
           print ("_"*89)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns | ")
           print ("_"*89) 
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|")  


                          
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("CHC", file))
           print ("-"*89) 
           print("\n") 
           
        elif teams == 'NYM':
           print ("_"*89)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns | ")
           print ("_"*89)  
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|")  
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("NYM", file))
           print ("-"*89) 
           print("\n")
           
        elif teams == 'BOS':
           print ("_"*91)    
           print ("|   Last names   | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns | ")
           print ("_"*91)  
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          print( "|",'{0:14}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|")  
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("BOS", file))
           print ("-"*91) 
           print("\n")
           
        elif teams == 'CWS':
           print ("_"*89)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns | ")
           print ("_"*89)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|")  
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("CWS", file))
           print ("-"*89) 
           print("\n")
           
        elif teams == 'WAS':
           print ("_"*89)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns | ")
           print ("_"*89)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|")  
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("WAS", file))
           print ("-"*89) 
           print("\n")

        elif teams == 'ATL':
           print ("_"*89)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns | ")
           print ("_"*89)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|")  
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("ATL", file))
           print ("-"*89) 
           print("\n")
           
        elif teams == 'PHI':
           print ("_"*89)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns | ")
           print ("_"*89)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|")  
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("PHI", file))
           print ("-"*89) 
           print("\n")

        elif teams == 'LAD':
           print ("_"*89)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns | ")
           print ("_"*89)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|")  
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("LAD", file))
           print ("-"*89) 
           print("\n")

        elif teams == 'TOR':
           print ("_"*89)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns | ")
           print ("_"*89)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|")  
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("TOR", file))
           print ("-"*89) 
           print("\n") 

        elif teams == 'KC':
           print ("_"*89)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns | ")
           print ("_"*89)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|")  
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("KC", file))
           print ("-"*89) 
           print("\n")

        elif teams == 'TEX':
           print ("_"*89)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns | ")
           print ("_"*89)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|")  
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("TEX", file))
           print ("-"*89) 
           print("\n") 
           
        elif teams == 'SF':
           print ("_"*89)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns | ")
           print ("_"*89)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|")  
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("SF", file))
           print ("-"*89) 
           print("\n")
           
        elif teams == 'CIN':
           print ("_"*89)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns | ")
           print ("_"*89)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|")  
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("CIN", file))
           print ("-"*89) 
           print("\n")
           
        elif teams == 'HOU':
           print ("_"*89)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns | ")
           print ("_"*89)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|")  
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("HOU", file))
           print ("-"*89) 
           print("\n")
           
        elif teams == 'ARI':
           print ("_"*89)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns | ")
           print ("_"*89)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|")  
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("ARI", file))
           print ("-"*89) 
           print("\n")
           
        elif teams == 'NYY':
           print ("_"*89)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns | ")
           print ("_"*89)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|")  
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("NYY", file))
           print ("-"*89) 
           print("\n")
           
        elif teams == 'MIL':
           print ("_"*89)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns | ")
           print ("_"*89)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|")  
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("MIL", file))
           print ("-"*89) 
           print("\n")
           
        elif teams == 'CLE':
           print ("_"*89)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns | ")
           print ("_"*89)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|")  
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("CLE", file))
           print ("-"*89) 
           print("\n")
           
        elif teams == 'STL':
           print ("_"*89)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns | ")
           print ("_"*89)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|")  
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("STL", file))
           print ("-"*89) 
           print("\n")
           
        elif teams == 'DET':
           print ("_"*89)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns | ")
           print ("_"*89)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|")  
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("DET", file))
           print ("-"*89) 
           print("\n")

        elif teams == 'LAA':
           print ("_"*89)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns | ")
           print ("_"*89)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|")   
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("LAA", file))
           print ("-"*89) 
           print("\n") 
           
        elif teams == 'SEA':
           print ("_"*89)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns | ")
           print ("_"*89)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|")  
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("SEA", file))
           print ("-"*89) 
           print("\n")
           
        elif teams == 'TB':
           print ("_"*89)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns | ")
           print ("_"*89)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|")  
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("TB", file))
           print ("-"*89) 
           print("\n")
           
        elif teams == 'OAK':
           print ("_"*89)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns | ")
           print ("_"*89)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|")  
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("OAK", file))
           print ("-"*89) 
           print("\n") 
           
        elif teams == 'PIT':
           print ("_"*89)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns | ")
           print ("_"*89)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|")  
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("PIT", file))
           print ("-"*89) 
           print("\n")
           
        elif teams == 'MIN':
           print ("_"*89)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns | ")
           print ("_"*89)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|")  
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("MIN", file))
           print ("-"*89) 
           print("\n") 

         
        else:
         print("I don't understand that choice, please try again.\n")


# REPORT : INFORMATION ABOUT HITS, BATTING AND SLUGGING        
        
    elif choice == 'REPORT':
        print("\nInformation about hits and batting")
        teams = input("Insert the name of your team to get the stats: ")
        print("\n")
        
        if teams =='BAL':
         print ("_"*77)    
         print ("| Last names | Fist names |  Bats | Hits | Doubles | Triples| Hruns |  SLG% |")
         print ("_"*77) 
         lista = [];
         def buscaPalabra(str, file):       
            for line in file:
                line = line.replace("\n", "")
                line = line.replace(";", "")
                line = line.replace(",", "")
              
                for part in line.split():
                   if str in part:
                       lista.append(line);
                       line = line.split()
                       linex = (int(line[6]) + int(line[7]) + (2*int(line[8])) + (3*int(line[9]))) / int(line[4])
                       new = round(linex,2)
                       print( "|",'{0:10}'.format(line[0]),"|",
                       '{0:10}'.format(line[1]),"|",
                       '{0:5}'.format (line[4]),"|",
                       '{0:4}'.format (line[6]),"|",
                       '{0:7}'.format (line[7]),"|",
                       '{0:6}'.format (line[8]),"|",
                       '{0:5}'.format (line[9]),"|",
                       '{0:5}'.format(new) ,"|")
    
            return lista
         file = open('2013.txt','r')
         (buscaPalabra("BAL", file))
         print ("-"*77) 
         print("\n")

        elif teams == 'CHC':
           print ("_"*97)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns |  SLG% |")
           print ("_"*97) 
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          linex = (int(line[6]) + int(line[7]) + (2*int(line[8])) + (3*int(line[9]))) / int(line[4])
                          new = round(linex,2)
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|",
                          '{0:5}'.format(new) ,"|")


                          
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("CHC", file))
           print ("-"*97) 
           print("\n")

        elif teams == 'NYM':
           print ("_"*97)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns |  SLG% | ")
           print ("_"*97)  
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          linex = (int(line[6]) + int(line[7]) + (2*int(line[8])) + (3*int(line[9]))) / int(line[4])
                          new = round(linex,2)
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|",
                          '{0:5}'.format(new) ,"|")      
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("NYM", file))
           print ("-"*97) 
           print("\n")
           
        elif teams == 'BOS':
           print ("_"*99)    
           print ("|   Last names   | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns |  SLG% | ")
           print ("_"*99)  
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          linex = (int(line[6]) + int(line[7]) + (2*int(line[8])) + (3*int(line[9]))) / int(line[4])
                          new = round(linex,2)
                          print( "|",'{0:14}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|",
                          '{0:5}'.format(new) ,"|") 
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("BOS", file))
           print ("-"*99) 
           print("\n")
           
        elif teams == 'CWS':
           print ("_"*97)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns |  SLG% | ")
           print ("_"*97)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          linex = (int(line[6]) + int(line[7]) + (2*int(line[8])) + (3*int(line[9]))) / int(line[4])
                          new = round(linex,2)
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|",
                          '{0:5}'.format(new) ,"|") 
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("CWS", file))
           print ("-"*97) 
           print("\n")
           
        elif teams == 'WAS':
           print ("_"*97)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns |  SLG% | ")
           print ("_"*97)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          linex = (int(line[6]) + int(line[7]) + (2*int(line[8])) + (3*int(line[9]))) / int(line[4])
                          new = round(linex,2)
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|",
                          '{0:5}'.format(new) ,"|")
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("WAS", file))
           print ("-"*97) 
           print("\n")

        elif teams == 'ATL':
           print ("_"*97)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns |  SLG% | ")
           print ("_"*97)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          linex = (int(line[6]) + int(line[7]) + (2*int(line[8])) + (3*int(line[9]))) / int(line[4])
                          new = round(linex,2)
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|",
                          '{0:5}'.format(new) ,"|")
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("ATL", file))
           print ("-"*97) 
           print("\n")
           
        elif teams == 'PHI':
           print ("_"*97)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns |  SLG% | ")
           print ("_"*97)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          linex = (int(line[6]) + int(line[7]) + (2*int(line[8])) + (3*int(line[9]))) / int(line[4])
                          new = round(linex,2)
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|",
                          '{0:5}'.format(new) ,"|")
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("PHI", file))
           print ("-"*97) 
           print("\n")

        elif teams == 'LAD':
           print ("_"*97)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns |  SLG% | ")
           print ("_"*97)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          linex = (int(line[6]) + int(line[7]) + (2*int(line[8])) + (3*int(line[9]))) / int(line[4])
                          new = round(linex,2)
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|",
                          '{0:5}'.format(new) ,"|")
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("LAD", file))
           print ("-"*97) 
           print("\n")

        elif teams == 'TOR':
           print ("_"*97)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns |  SLG% | ")
           print ("_"*97)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          linex = (int(line[6]) + int(line[7]) + (2*int(line[8])) + (3*int(line[9]))) / int(line[4])
                          new = round(linex,2)
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|",
                          '{0:5}'.format(new) ,"|")    
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("TOR", file))
           print ("-"*97) 
           print("\n") 

        elif teams == 'KC':
           print ("_"*97)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns |  SLG% | ")
           print ("_"*97)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          linex = (int(line[6]) + int(line[7]) + (2*int(line[8])) + (3*int(line[9]))) / int(line[4])
                          new = round(linex,2)
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|",
                          '{0:5}'.format(new) ,"|")
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("KC", file))
           print ("-"*97) 
           print("\n")

        elif teams == 'TEX':
           print ("_"*97)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns |  SLG% | ")
           print ("_"*97)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          linex = (int(line[6]) + int(line[7]) + (2*int(line[8])) + (3*int(line[9]))) / int(line[4])
                          new = round(linex,2)
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|",
                          '{0:5}'.format(new) ,"|")
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("TEX", file))
           print ("-"*97) 
           print("\n") 
           
        elif teams == 'SF':
           print ("_"*97)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns |  SLG% | ")
           print ("_"*97)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          linex = (int(line[6]) + int(line[7]) + (2*int(line[8])) + (3*int(line[9]))) / int(line[4])
                          new = round(linex,2)
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|",
                          '{0:5}'.format(new) ,"|")
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("SF", file))
           print ("-"*97) 
           print("\n")
           
        elif teams == 'CIN':
           print ("_"*97)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns |  SLG% | ")
           print ("_"*97)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          linex = (int(line[6]) + int(line[7]) + (2*int(line[8])) + (3*int(line[9]))) / int(line[4])
                          new = round(linex,2)
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|",
                          '{0:5}'.format(new) ,"|")
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("CIN", file))
           print ("-"*97) 
           print("\n")
           
        elif teams == 'HOU':
           print ("_"*97)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns |  SLG% | ")
           print ("_"*97)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          linex = (int(line[6]) + int(line[7]) + (2*int(line[8])) + (3*int(line[9]))) / int(line[4])
                          new = round(linex,2)
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|",
                          '{0:5}'.format(new) ,"|")
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("HOU", file))
           print ("-"*97) 
           print("\n")
           
        elif teams == 'ARI':
           print ("_"*97)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns |  SLG% | ")
           print ("_"*97)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          linex = (int(line[6]) + int(line[7]) + (2*int(line[8])) + (3*int(line[9]))) / int(line[4])
                          new = round(linex,2)
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|",
                          '{0:5}'.format(new) ,"|")
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("ARI", file))
           print ("-"*97) 
           print("\n")
           
        elif teams == 'NYY':
           print ("_"*97)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns |  SLG% | ")
           print ("_"*97)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          linex = (int(line[6]) + int(line[7]) + (2*int(line[8])) + (3*int(line[9]))) / int(line[4])
                          new = round(linex,2)
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|",
                          '{0:5}'.format(new) ,"|")
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("NYY", file))
           print ("-"*97) 
           print("\n")
           
        elif teams == 'MIL':
           print ("_"*97)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns |  SLG% | ")
           print ("_"*97)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          linex = (int(line[6]) + int(line[7]) + (2*int(line[8])) + (3*int(line[9]))) / int(line[4])
                          new = round(linex,2)
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|",
                          '{0:5}'.format(new) ,"|")
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("MIL", file))
           print ("-"*97) 
           print("\n")
           
        elif teams == 'CLE':
           print ("_"*97)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns |  SLG% | ")
           print ("_"*97)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          linex = (int(line[6]) + int(line[7]) + (2*int(line[8])) + (3*int(line[9]))) / int(line[4])
                          new = round(linex,2)
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|",
                          '{0:5}'.format(new) ,"|")
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("CLE", file))
           print ("-"*97) 
           print("\n")
           
        elif teams == 'STL':
           print ("_"*97)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns |  SLG% | ")
           print ("_"*97)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          linex = (int(line[6]) + int(line[7]) + (2*int(line[8])) + (3*int(line[9]))) / int(line[4])
                          new = round(linex,2)
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|",
                          '{0:5}'.format(new) ,"|")
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("STL", file))
           print ("-"*97) 
           print("\n")
           
        elif teams == 'DET':
           print ("_"*97)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns |  SLG% | ")
           print ("_"*97)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          linex = (int(line[6]) + int(line[7]) + (2*int(line[8])) + (3*int(line[9]))) / int(line[4])
                          new = round(linex,2)
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|",
                          '{0:5}'.format(new) ,"|")
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("DET", file))
           print ("-"*97) 
           print("\n")

        elif teams == 'LAA':
           print ("_"*97)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns |  SLG% | ")
           print ("_"*97)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          linex = (int(line[6]) + int(line[7]) + (2*int(line[8])) + (3*int(line[9]))) / int(line[4])
                          new = round(linex,2)
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|",
                          '{0:5}'.format(new) ,"|")
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("LAA", file))
           print ("-"*97) 
           print("\n") 
           
        elif teams == 'SEA':
           print ("_"*97)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns |  SLG% | ")
           print ("_"*97)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          linex = (int(line[6]) + int(line[7]) + (2*int(line[8])) + (3*int(line[9]))) / int(line[4])
                          new = round(linex,2)
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|",
                          '{0:5}'.format(new) ,"|")
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("SEA", file))
           print ("-"*97) 
           print("\n")
           
        elif teams == 'TB':
           print ("_"*97)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns |  SLG% | ")
           print ("_"*97)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          linex = (int(line[6]) + int(line[7]) + (2*int(line[8])) + (3*int(line[9]))) / int(line[4])
                          new = round(linex,2)
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|",
                          '{0:5}'.format(new) ,"|")
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("TB", file))
           print ("-"*97) 
           print("\n")
           
        elif teams == 'OAK':
           print ("_"*97)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns |  SLG% | ")
           print ("_"*97)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          linex = (int(line[6]) + int(line[7]) + (2*int(line[8])) + (3*int(line[9]))) / int(line[4])
                          new = round(linex,2)
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|",
                          '{0:5}'.format(new) ,"|")
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("OAK", file))
           print ("-"*97) 
           print("\n") 
           
        elif teams == 'PIT':
           print ("_"*97)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns |  SLG% | ")
           print ("_"*97)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          linex = (int(line[6]) + int(line[7]) + (2*int(line[8])) + (3*int(line[9]))) / int(line[4])
                          new = round(linex,2)
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|",
                          '{0:5}'.format(new) ,"|")
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("PIT", file))
           print ("-"*97) 
           print("\n")
           
        elif teams == 'MIN':
           print ("_"*97)    
           print ("|  Last names  | Fist names | Gplayed | Bats | Rscores| Hits | Doubles | Triples| Hruns |  SLG% | ")
           print ("_"*97)   
           lista = [];
           def buscaPalabra(str, file):       
               for line in file:
                   line = line.replace("\n", "")
                   line = line.replace(";", "")
                   line = line.replace(",", "")
                   for part in line.split():            
                       if str in part:                
                          lista.append(line);
                          line = line.split()
                          linex = (int(line[6]) + int(line[7]) + (2*int(line[8])) + (3*int(line[9]))) / int(line[4])
                          new = round(linex,2)
                          print( "|",'{0:12}'.format(line[0]),"|",
                          '{0:10}'.format(line[1]),"|",
                          '{0:7}'.format (line[3]),"|",
                          '{0:4}'.format (line[4]),"|",
                          '{0:6}'.format (line[5]),"|",
                          '{0:4}'.format (line[6]),"|",
                          '{0:7}'.format (line[7]),"|",
                          '{0:6}'.format (line[8]),"|",
                          '{0:5}'.format (line[9]),"|",
                          '{0:5}'.format(new) ,"|")
               return lista
           file = open('2013.txt','r')
           (buscaPalabra("MIN", file))
           print ("-"*97) 
           print("\n") 

         
        else:
         print("I don't understand that choice, please try again.\n")
         

#HELP: MORE INFORMATION
    elif choice == 'HELP':
        print("Remember, that you can see the stats of your favorite team by typing the abrevation")
        print("Example: If you want to choose Boston Rex Sox, you just need to type: 'BOS' ")
        print("The teams are:")
        print ("BAL:Baltimore Orioles")
        print ("CHC:Chicago Cubs")
        print ("NYM:New York Mets")
        print ("BOS:Boston Red Sox")
        print ("CWS:Chicago White Sox")
        print ("WAS:Washington Nationals")
        print ("ATL:Atlanta Braves")
        print ("PHI:Philadelphia Phillies")
        print ("LAD:Los Angeles Dodgers")
        print ("TOR:Toronto Blue Jays")
        print ("KC:Kansas City Royals")
        print ("TEX:Texas Rangers")
        print ("SF:San Francisco Giants")
        print ("CIN:Cincinnati Reds")
        print ("HOU:Houston Astros")
        print ("ARI:Arizona Diamondbacks")
        print ("NYY:New York Yankees")
        print ("MIL:Milwaukee Brewers")
        print ("CLE:Cleveland Indians ")
        print ("STL:St. Louis Cardinals")
        print ("DET:Detroit Tigers")
        print ("LAA:Los Angeles Angels of Anaheim")
        print ("SEA:Seattle Mariners")
        print ("TB:Tampa Bay Rays")
        print ("OAK:Oakland Athletics")
        print ("PIT:Pittsburgh Pirates")
        print ("MIN:Minnesota Twins")
       
        


        
       
# QUIT: TO  LEAVE THE PROGRAM

    elif choice == 'QUIT':
        print("\nThanks for playing. See you later.\n")
        print (" ** Created by : Jenniffer Kwiatkowski and Pedro Canchari Palomino. **")
        print (" ** November 2016 **\n")
    else:
        print("\nI don't understand that choice, please try again.\n")
        
print("Thanks again, bye now.\n")        



