import numpy as np
import matplotlib.pyplot as plt
# NO other imports are allowed

class Shape: 
    '''
    DO NOT MODIFY THIS CLASS

    DO NOT ADD ANY NEW METHODS TO THIS CLASS
    '''
    def __init__(self): #This is the instantiation function of the class Shape. As an instance of this class is called, these variables are assigned to the instance.
        self.T_s = None
        self.T_r = None
        self.T_t = None
    
    
    def translate(self, dx, dy): #The linear transformation function for translation of a 2-D point is mentioned in the array given below. 
        '''
        Polygon and Circle class should use this function to calculate the translation
        '''
        self.T_t = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]]) #The variable self.T_t gets assigned with the translation matrix and can be used for calculations.
        

    def scale(self, sx, sy): #The linear transformation function for scaling of a 2-D point is mentioned in the array given below.
        '''
        Polygon and Circle class should use this function to calculate the scaling
        '''
        self.T_s = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]]) #The variable self.T_s gets assigned with the scaling matrix and can be used for calculations.
 
        
    def rotate(self, deg): #The linear transformation function for rotation of a 2-D point is mentioned in the array given below.
        '''
        Polygon and Circle class should use this function to calculate the rotation
        '''
        rad = deg*(np.pi/180) #Converting degrees to radians.
        self.T_r = np.array([[np.cos(rad), np.sin(rad), 0],[-np.sin(rad), np.cos(rad),0], [0, 0, 1]]) #The variable self.T_r gets assigned with the rotation matrix and can be used for calculations.

        
    def plot(self, x_dim, y_dim): #This function helps in plotting the graph of the given function. 
        '''
        Polygon and Circle class should use this function while plotting
        x_dim and y_dim should be such that both the figures are visible inside the plot
        '''
        x_dim, y_dim = 1.2*x_dim, 1.2*y_dim
        plt.plot((-x_dim, x_dim),[0,0],'k-')
        plt.plot([0,0],(-y_dim, y_dim),'k-')
        plt.xlim(-x_dim,x_dim) 
        plt.ylim(-y_dim,y_dim) #The upper and lower limits of the plot are assigned using this function.
        plt.grid() #The grid of the plot appears
        plt.show() #The plot is shown, with whatever has been plotted in it.



class Polygon(Shape): #This is the class Polygon. All operations that will happen for the Polygon inputs will take place here.
    '''
    Object of class Polygon should be created when shape type is 'polygon'
    '''
    def __init__(self, A): #The instantiation of the class comes with the following variables.
        '''
        Initializations here
        '''
        Shape.__init__(self) #Calling the parent class Shape and instantiating variables from there as well.
        self.array = np.array(A) #The array inputted into the class is instantiated right here. It is an (nx3) matrix containing n vertices of the polygon.


 
    
    def translate(self, dx, dy):
        '''
        Function to translate the polygon
    
        This function takes 2 arguments: dx and dy
    
        This function returns the final coordinates
        '''
        for i in range(len(self.array)): #For all the individual vertices in self.array,

            Shape.translate(self, dx, dy) #Called to reassign the value of self.T_t to the translation matrix, as mentioned in class Shape.

            self.array[i] = np.dot(self.T_t,np.transpose(self.array[i])).round(2) #Multiplication of 2 matrices, one is the translation matrix and the other is a vertex of the polygon.
            #The resulting array is rounded off to 2 decimal places.
        
        return tuple(np.transpose(self.array))[:-1] #All the vertices are translated and the x-values and corresponding y-values of the transpose are returned.




    
    def scale(self, sx, sy):
        '''
        Function to scale the polygon
    
        This function takes 2 arguments: sx and sx
    
        This function returns the final coordinates
        '''
        centre = np.transpose(self.array)

        x_centre = sum(centre[0])/len(centre[0])

        y_centre = sum(centre[1])/len(centre[1]) #The values of the centre of the polygon are found. They are the algebraic average of the vertices of the polygon.
        
        modified = np.array(Polygon.translate(self,-x_centre,-y_centre)) #As scaling is done from the centre of the polygon, the matrix is being translated such that the centre is the origin.
        #If the centre of the polygon lies in the origin, the scaling matrix can be used to scale each vertex of the polygon.

        self.array = np.transpose(modified) #Here, self.array is an (nx2) matrix as it is taken from the Polygon.translate() function.
        
        temp = []

        for i in range(len(self.array)):

            temp.append(list(self.array[i])+[1.0])

        self.array = np.array(temp) #Converts self.array back to an (nx3) matrix from an (nx2) matrix.

        for i in range(len(self.array)): #For each vertex in self.array,

            Shape.scale(self, sx, sy)

            k = np.dot(self.T_s,np.transpose(self.array[i])) #The scaling matrix is multiplied with each vertex, thus scaling it from the origin.

            self.array[i] = list(k) #After the end of the for loop, the matrix self.array remains an (nx3) matrix.
        
        modified = np.array(Polygon.translate(self,x_centre,y_centre)) #The polygon is retreanslated to its original centre coordiantes.

        #The basic concept used in the function is that when a polygon is scaled, the centre of the polygon does not change its coordinates.
        
        return tuple(modified)




 
    
    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the polygon
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates
        '''
        if not(rx == 0 and ry == 0): #To save on complexity of the program, an initial check whether the point of rotation is (0,0) or not.
            
            modified = np.array(Polygon.translate(self,-rx,-ry)) #If the point is not (0,0), translation of the polygon to the origin.

            self.array = np.transpose(modified)

            temp = []

            for i in range(len(self.array)):

                temp.append(list(self.array[i])+[1.0])

            self.array = np.array(temp) #Converting self.array from (nx2) to and (nx3) matrix.

        for i in range(len(self.array)): #For every vertex in self.array,

            Shape.rotate(self, deg)

            k = np.dot(self.T_r,np.transpose(self.array[i])) #Rotation of the point (about the origin in all these cases, as the points have been translated)

            self.array[i] = list(k) 
            
        modified = np.array(Polygon.translate(self,rx,ry)) #Translation of the point back by a factor of (rx,ry), as it was initially translated.
        #Even if the point wasn't translated initially, it will be translated by a factor of (0,0), thus making no difference to the output.
        #modified is a (2xn) matrix.
        
        return tuple(modified)
        



    

    def plot(self):
        '''
        Function to plot the polygon
    
        This function should plot both the initial and the transformed polygon
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''

        modified = np.transpose(self.array) #To obtain all x-values and y-values of the polygon as a list.

        plt.plot(modified[0],modified[1], color = "black") #To plot (n-1) sides of a polygon in the order of the x-vals and y-vals.

        plt.plot([modified[0][-1],modified[0][0]],[modified[1][-1],modified[1][0]],color = "black") #To plot the last line of the polygon, joining the last vertex and first vertex.
        
        x_dim, y_dim = 0,0

        for i in modified[0]: 

            if x_dim < abs(i):

                x_dim = abs(i)

        for i in modified[1]:

            if y_dim < abs(i):
                
                y_dim = abs(i) #This algorithm figures out the coordinates of the limits of the graph when plotted.
                #The absolute value of the elements of the vertices are used as the graph extends to both ends.

        x_temp,y_temp = x_dim,y_dim #The value of the limits of the graph to be plotted.

        if flag == True or (verbose == 1 and l1[0] != "P"): #The conditions necessary for plotting just the initial graph, and not the previous graph as well.

            modified = np.transpose(initial_coordinates.array) #To obtain all x-values and y-values of the previous polygon as a list.

            plt.plot(modified[0],modified[1],linestyle = "--", color = "gray") #To plot (n-1) sides of a polygon in the order of the x-vals and y-vals.

            plt.plot([modified[0][-1],modified[0][0]],[modified[1][-1],modified[1][0]],linestyle = "--", color = "gray") #To plot the last line of the polygon, joining the last vertex and first vertex.
        
            x_dim, y_dim = 0,0

            for i in modified[0]: 

                if x_dim < abs(i):

                    x_dim = abs(i)

            for i in modified[1]:

                if y_dim < abs(i):
                    
                    y_dim = abs(i) #This algorithm figures out the coordinates of the limits of the graph when plotted. The absolute value of the elements of the vertices are used as the graph extends to both ends.

            x_og,y_og = x_dim,y_dim #The value of the limits of the previous graph to be plotted.

            Shape.plot(coordinates,max(x_temp,x_og), max(y_temp,y_og)) #Takes the maximum of both the previous and current plots.

        else:

            Shape.plot(coordinates,x_temp, y_temp) #Takes the initial instance's value.
        
        






class Circle(Shape):
    '''
    Object of class Circle should be created when shape type is 'circle'
    '''

    
    
    def __init__(self, x=0, y=0, radius=5): 
        '''
        Initializations here
        '''
        Shape.__init__(self) #This calls the parent class Shape and initializes the variables present in that with the current class.
        self.array = [x,y,1]
        self.attributes = [x,y,radius]

        

    
    def translate(self, dx, dy):
        '''
        Function to translate the circle
    
        This function takes 2 arguments: dx and dy (dy is optional).
    
        This function returns the final coordinates and the radius
        '''                
        Shape.translate(self, dx, dy) 

        self.array = np.dot(self.T_t,np.transpose(np.array(self.array))) #Multiplying the translation matrix by the cenrte coordinates of the circle.

        self.attributes[0],self.attributes[1] = round(self.array[0],2),round(self.array[1],2) #Updating the coordinates of the centre of the circle and rounding off upto 2 decimal place.

        return tuple(self.attributes) #Returns a 2-element tuple.



    
         
    def scale(self, sx):
        '''
        Function to scale the circle
    
        This function takes 1 argument: sx
    
        This function returns the final coordinates and the radius
        '''
        self.attributes[2] = round(self.attributes[2]*sx,2) #Simply multiplies the radius of the circle by 2 and rounds it off.
        
        return tuple(self.attributes)




 
    
    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the circle
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates and the radius
        '''
        Shape.rotate(self, deg)

        if not(rx == 0 and ry == 0):

            Circle.translate(self,-rx,-ry) #In case the rotation is not about the origin, this condition makes the code more efficient.
            #It translates the point in such a way that the rotation now happens around the origin.

        self.array = np.dot(self.T_r,np.transpose(np.array(self.array)))#This statement multiplies the rotation matrix with the coordinates of the centre of the circle.
        #The algorithm ensures that this point is always rotated about the origin.
        
        Circle.translate(self,rx,ry) #This statement re-translates the point back to the original point from the origin.

        self.attributes[0],self.attributes[1] = round(self.array[0],2),round(self.array[1],2) #Rounding off the points and modifying the self.attributes array.

        return tuple(self.attributes) #Returns the x-value, y-value and radius, respectively.
 




    
    def plot(self):
        '''
        Function to plot the circle
    
        This function should plot both the initial and the transformed circle
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''

        tester = np.arange(0,2*np.pi,0.01) #Values from 0 to 2pi, to ensure all values of sine and cosine are evaluated.

        xvals = (self.attributes[2]*np.cos(tester))+self.array[0] 

        yvals = (self.attributes[2]*np.sin(tester))+self.array[1] #Uses parametric form to determine the x-values and y-values of the circle.

        plt.plot(xvals,yvals,color = "black")

        if self.array[0] > 0:

            x_dim = self.array[0] + self.attributes[2]

        else:

            x_dim = abs(self.array[0] - self.attributes[2])

        if self.array[1] > 0:

            y_dim = self.array[1] + self.attributes[2]

        else:

            y_dim = abs(self.array[1] - self.attributes[2]) #Calculates the values of the dimensions of the graph as required in the Shape.plot() function.

        x_temp,y_temp = x_dim,y_dim

        if flag == True or (verbose == 1 and l1[0] != "P"): #The conditions necessary for plotting just the initial graph, and not the previous graph as well.

            tester = np.arange(0,2*np.pi,0.01) #Values from 0 to 2pi, to ensure all values of sine and cosine are evaluated.

            xvals = (initial_coordinates.attributes[2]*np.cos(tester))+initial_coordinates.array[0] #Uses the instance initial_coordinates to plot the value of the previous state of the plot.

            yvals = (initial_coordinates.attributes[2]*np.sin(tester))+initial_coordinates.array[1] #Uses parametric form to determine the x-values and y-values of the circle.

            plt.plot(xvals,yvals,color = "gray", linestyle = "--") #Plots the graph using the conditions for plotting the previous graph.

            if initial_coordinates.array[0] > 0:

                x_dim = initial_coordinates.array[0] + initial_coordinates.attributes[2]

            else:

                x_dim = abs(initial_coordinates.array[0] - initial_coordinates.attributes[2])

            if initial_coordinates.array[1] > 0:

                y_dim = initial_coordinates.array[1] + initial_coordinates.attributes[2]

            else:

                y_dim = abs(initial_coordinates.array[1] - initial_coordinates.attributes[2]) #Calculates the values of the dimensions of the graph as required in the Shape.plot() function.

            x_og,y_og = x_dim,y_dim 

            Shape.plot(coordinates,max(x_temp,x_og), max(y_temp,y_og)) #Takes the maximum of both the previous and current plots.

        else:

            Shape.plot(coordinates,x_temp, y_temp) #Takes the initial instance's value.




        

if __name__ == "__main__": #The main loop of the program.
    '''
    Add menu here as mentioned in the sample output section of the assignment document.
    '''

    verbose = int(input("verbose? 1 to plot, 0 otherwise: ")) 

    for x in range(int(input("Enter the number of test cases: "))): #Runs a loop for the number of test cases.

        flag = False #This is a checker function which is basically for the verbose = 1 and plot functions. The flag value is False only for the first iteration of the query loop.
        #As soon as one round of queries are over, the flag value changes to True.

        shape = int(input("Enter type of shape (polygon/circle): ")) #Either 0 or 1.

        if shape == 0:

            l = []

            for y in range(int(input("Enter the number of sides: "))):

                v = list(map(float,input(f"enter (x{y+1}, y{y+1}): ").split()))

                for r in range(len(v)):

                    v[r] = round(v[r],2)

                l.append(v+[1.0]) #Initializing a list of the coordinates of the initial polygon. Hence appending them in the same order to a list to perform the queries asked by the user.

            initial_coordinates = Polygon(l) #This instance is used for plotting the dotted gray plot of the graph. Its value remains predecessing plot of the function.
                
            z = int(input("Enter the number of queries: "))

            print("""Enter Query:
1) R  deg (rx) (ry)
2) T dx (dy)
3) S sx (sy)
4) P""") #Asking for the inputs of queries from the user.
                
            for w in range(z): #The query loop

                coordinates = Polygon(l) #Instantiating the main class of the polygon. Here is where all the main queries will be performed and this instance will be edited after every iteration of the query loop.

                l1 = list(map(str,input().split())) #This list takes in the value of the query followed by the parameters of the query, space seperated.

                if l1[0] != "P" and verbose == 0: #This condition ensures that the output is not printed for the user when the plotting of the polygons are done in the program.

                    for j in np.transpose(l)[:-1]: #Prints the x-values and the y-values of the current state of the polygon.

                        print(*j, end = " ")

                    print()
                    
#I am only explaining the functionality of one of the queries. This is because all queries have a fucntionality very similar to that of each other. 

                if l1[0] == "R": #The rotate function of the polygon.

                    initial_coordinates = Polygon(l) #The instantiation of the previous state of the polygon.                     

                    if len(l1) == 2:

                        array = np.array(coordinates.rotate(float(l1[1])))

                    elif len(l1) == 4:

                        array = np.array(coordinates.rotate(float(l1[1]),float(l1[2]),float(l1[3]))) #Calls the rotate function based on the number of parameters provided and stores the returned value in an array.

                    if verbose == 0:

                        for i in array: #Prints the resulting array of x-vals and y-vals. If verbose = 0

                            print(*i, end = " ")

                        print()

                    else:

                        coordinates.array = np.transpose(array)

                        coordinates.plot() #Calls the plot function if verbose = 1.

                elif l1[0] == "T": #The translate function of the polygon.
                
                    initial_coordinates = Polygon(l) 

                    if len(l1) == 2:

                        array = np.array(coordinates.translate(float(l1[1]),float(l1[1])))

                    elif len(l1) == 3:

                        array = np.array(coordinates.translate(float(l1[1]),float(l1[2])))

                    if verbose == 0:

                        for i in list(array):

                            print(*i, end = " ")

                        print()

                    else:

                        coordinates.array = np.transpose(array)

                        coordinates.plot()

                elif l1[0] == "S": #The scaling function of the polygon.

                    initial_coordinates = Polygon(l)

                    if len(l1) == 2:

                        array = np.array(coordinates.scale(float(l1[1]),float(l1[1])))

                    elif len(l1) == 3:

                        array = np.array(coordinates.scale(float(l1[1]),float(l1[2])))

                    if verbose == 0:

                        for i in array:

                            print(*i,end = " ")

                        print()

                    else:

                        coordinates.array = np.transpose(array)

                        coordinates.plot()

                elif l1[0] == "P": #The plotting function of the polygon.

                    array = np.transpose(np.array(l))[:-1] #It modifies the variable array to a similar format as in the other queries.
                    
                    coordinates.plot() #Calling the plot function.

                    initial_coordinates = Polygon(l) #Instantiates the previous polygon for plotting purposes.
                    
                l = []

                for x in np.transpose(array):

                    l.append(list(x)+[1.0]) #Reinitializing the value of the list to the updated value, in the correct format.

                flag = True #Changling flag to True, as the loop has run once.

        elif shape == 1: #For the shape circle

            l = list(map(float,input("enter (centre(x), centre(y), radius): ").split()))  #Inputting the value of the initial coordianates of the circle

            for r in range(len(l)): #For rounding off the list of coordinates provided and re-appending to this list.

                l[r] = round(l[r],2)

            initial_coordinates = Circle(*l) #Creating the previous instance, for the plotting function of the polygon.

            z = int(input("Enter the number of queries: ")) #Number of queries

            print("""Enter Query:
1) R  deg (rx) (ry)
2) T dx (dy)
3) S sr
4) P""")
                
            for w in range(z): #For the number of queries asked,

                coordinates = Circle(*l) #Instantiation of the current variable for performing the queries asked for in the polygon functions.

                l1 = list(map(str,input().split())) #Inputting the queries asked for.

                if l1[0] != "P" and verbose == 0: 

                    if len(l) == 1:

                        print(l[0],0.0,5.0)

                    elif len(l) == 2:

                        print(l[0],l[1],5.0)

                    else:

                        for j in np.array(l):

                            print(j, end = " ") #This condition checks for whether there is a need to plot the points of the previous instance of the graph or not. 
#If the function does not have a verbose = 1 and the plot function is not called, this condition will execute.

                        print()
                        
#I shall only explain the working of one condition of the query loop, as the functionality of all the quries is very similar.

                if l1[0] == "R": #The rotation query of the circle.

                    initial_coordinates = Circle(*l) #Re-instantiating the value of the previous coordinates of the circle, in order to plot the previous points if necessary.

                    if len(l1) == 2:

                        array = np.array(coordinates.rotate(float(l1[1])))

                    elif len(l1) == 4:

                        array = np.array(coordinates.rotate(float(l1[1]),float(l1[2]),float(l1[3]))) #Checking for how many parameters have been provided in the input, and calling the function of the class according to that input.

                    if verbose == 0:

                        for i in array:

                            print(i, end = " ")

                        print() #Printing the value of the coordinates if the verbose = 0.

                    else:

                        coordinates.array = array

                        coordinates.plot() #Plotting the graphs of the cirlces if the verbose = 1.
                        

                elif l1[0] == "T": #The translate function of the circle.

                    initial_coordinates = Circle(*l)

                    if len(l1) == 2:

                        array = np.array(coordinates.translate(float(l1[1]),float(l1[1])))

                    elif len(l1) == 3:

                        array = np.array(coordinates.translate(float(l1[1]),float(l1[2])))

                    if verbose == 0:

                        for i in array:

                            print(i, end = " ")

                        print()

                    else:

                        coordinates.array = array

                        coordinates.plot()

                elif l1[0] == "S": #The scaling function of the circle.

                    initial_coordinates = Circle(*l)

                    array = np.array(coordinates.scale(float(l1[1])))

                    if verbose == 0:

                        for i in array:

                            print(i, end = " ")

                        print()

                    else:

                        coordinates.array = array

                        coordinates.plot()

                elif l1[0] == "P": #The plotting function of the circle.

                    array = l #Getting the value of the variable array in the same format as in the rest of the queries.

                    coordinates.plot() #Calling the plot function for the coordinates instance.

                    initial_coordinates = Circle(*l) #Re-initializing the value of the previous instance to that of the current instance, so that it remains so in the next iteration of the loop.

                l = list(array) #Creating an array of the list, so that array functions can be performed on it.

                flag = True #Setting flag to True after one iteration of the main loop.
