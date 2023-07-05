#Python Stack


a_list_stack = [1, 2, 3] #리스트 지정
a_list_stack.append(4) #리스트 요소 추가

print(a_list_stack) #리스트 호출



b_list_stack = [1, 2, 3] #리스트 지정
b_list_stack.pop() #리스트 요소 빼기

print(b_list_stack) #리스트 호출

#예시?
WebBrowserData = ["1page","2page","3page"] #웹페이지 방문 기록
WebBrowserData.append("4page") #새로 방문한 웹 페이지

print(WebBrowserData) #바ㅏ지막에 방문한 웹페이지 방문기록에 추가

T_WebBrowserData = ["1page", "2page", "3page"] #웹페이지 방문기록
t = T_WebBrowserData [-1] #마지막으로 방문한 웹페이지 출력

print(t) #출력