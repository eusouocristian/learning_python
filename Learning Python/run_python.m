commandStr = 'python C:/Users/Cristian/Dropbox/Python/hello.py';
[status, commandOut] = system(commandStr);
if status==0
    fprintf('The result is %sa\n',commandOut);
end