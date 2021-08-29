module DynamicalArrays
  implicit none
  
  contains

      subroutine AddToList(list, element)
      !routine to add an element to a dynamic array

          IMPLICIT NONE
          
          integer :: i, isize, errCode
          integer, intent(in) :: element
          integer, dimension(:), allocatable, intent(inout) :: list
          integer, dimension(:), allocatable :: clist

          
          if(allocated(list)) then
              isize = size(list)
              allocate(clist(isize+1),stat = errCode)
              
              do i=1,isize          
                clist(i) = list(i)
              end do
              clist(isize+1) = element
              
              deallocate(list)
              
              call move_alloc(clist, list)

          else
              
              allocate(list(1))
              list(1) = element
          end if
          
          
      end subroutine AddToList


  end module DynamicalArrays

logical function isCycle(cycleList,list_Length) result(tf)
  !determine if a list contains a cycle
  implicit none
  integer             :: i
  integer, intent(in) :: list_Length
  integer, dimension(list_Length), intent(in):: cycleList
  integer, dimension(list_Length-1) :: list_Copy
  do i=1,list_Length-1
    list_Copy(i)=cycleList(i)
  end do
  if(any(list_Copy == cycleList(list_length)))then
    tf = .TRUE.
  else
    tf = .FALSE.
  end if
    
end function isCycle 
    
 
integer function getSteps(input,cycleStyle,m,a,MAX_VALUE) result(steps)
  ! get the number of steps in a trajectory for a starting number
  ! or get the length of a cycle for a starting number
  use DynamicalArrays
  implicit none
  
          
          
  integer, intent(in)    :: m,a
  integer(kind=8)        :: MAX_VALUE
  logical, intent(in)    :: cycleStyle
  logical                :: isCycle
  
  integer, intent(in)    :: input
  integer                :: status,x
  integer, dimension(:),allocatable :: cycleList
  status = 0
  steps = 0
  x = input
  call AddToList(cycleList,x)
  do while(x .NE. 1)
    
    !print*,"pp",x,steps
    if(x>MAX_VALUE)then
      status = 1
      print *, "Abort: value too large"
      call EXIT(status)
    else if(abs(mod(x,2))==1) then
      
      x = m*x+a
      steps = steps + 1
      call AddToList(cycleList,x)
      
      
    else if(mod(x,2)==0) then
      
      x = x/2
      
      steps = steps + 1
      call AddToList(cycleList,x)
      
    end if
    if(cycleStyle) then
      if(isCycle(cycleList,size(cycleList))) then  
        
        
        steps = -1*size(cycleList)
        
        exit
        
      end if
      
    end if
    
  end do
  deallocate(cycleList)
end function getSteps

    	

subroutine get_Steps_List(N,m,a,cycleStyle)
  ! produce steps list for all values in an input range and write them to file 
  use DynamicalArrays
  implicit none
  integer(kind=8)     :: MAX_VAlUE
  integer, intent(in) :: N,m,a
  integer             :: getSteps,l
  integer, dimension(-N:N) :: step_List
  logical                 :: cycleStyle
  character(len=100) :: file_name
  MAX_VALUE = huge(0_8)
  l = -1*N
  
  
  do while(l<=N)
    
    step_List(l) = getSteps(l,cycleStyle,m,a,MAX_VALUE)
    
    l = l+1
    
  end do
  
  write (file_name,"('Collatz_Fortran',i0,'.dat')") N
  
  open(10,file=trim(file_name),action = "write")
  do l=-1*N,N
    
    write(10,*) step_List(l) 
  end do
  close(10)
  return
end subroutine get_Steps_List



program collatz_Main !time to finish for different starting ranges is found
  use DynamicalArrays
  implicit none
  integer :: i
  real :: start, finish
  do i=1,6 
    call cpu_time(start) 
    call get_Steps_List(10**i,-3,-1,.TRUE.)    
    call cpu_time(finish)
    print '("N =", i0)', 10**i
    print '("Time = ",f10.3," seconds.")',finish-start
    print *, " "
  end do
  
  
end program collatz_Main




