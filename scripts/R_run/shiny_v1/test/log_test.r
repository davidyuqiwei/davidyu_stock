library(logging)
basicConfig()
    
#ls(getLogger())
#with(getLogger(), level)
#with(getLogger(), names(handlers))
#loginfo('does it work?')
#logwarn('%s %d', 'my name is', 5)
#logdebug('I am a silent child')


basicConfig(level='ERROR')
addHandler(writeToFile, file="~/testing.log", level='ERROR')
#with(getLogger(), names(handlers))
loginfo('test %d', 1)
logdebug('test %d', 2)
logwarn('test %d', 3)
logerror("error")
logfinest('test %d', 4)



