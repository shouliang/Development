// 展示如何写一个表组测试
package listing08

import (
	"net/http"
	"testing"
)

const (
	checkMark = "\u2713"
	ballotX   = "\u2717"
)

func TestDownload(t *testing.T) {
	var urls = []struct {
		url        string
		statusCode int
	}{
		{
			"https://www.baidu.com",
			http.StatusOK,
		},
		{
			"https:www.google.com",
			http.StatusNotFound,
		},
	}

	t.Log("Given the need to test downloading content.")
	{
		for _, u := range urls {
			t.Logf("\tWhen checking \"%s\" for status code \"%d\"", u.url, u.statusCode)
			{
				resp, err := http.Get(u.url)
				if err != nil {
					t.Fatal("\t\tShould be able to make the Get call.", ballotX, err)
				}
				t.Log("\t\tShould be able to make the Get call.", checkMark)

				defer resp.Body.Close()

				if resp.StatusCode == u.statusCode {
					t.Logf("\t\tShould receive a \"%d\" status. %v", u.statusCode, checkMark)
				} else {
					t.Errorf("\t\tShould receive a \"%d\" status. %v %v", u.statusCode, ballotX, resp.Status)
				}
			}
		}
	}

}
